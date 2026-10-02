from flask import Blueprint, render_template, request, redirect, url_for, flash
import razorpay
import os

payment_bp = Blueprint("payment", __name__, url_prefix="/payment")


# =========================================================
# RAZORPAY TEST MODE KEYS
# =========================================================
RAZORPAY_KEY_ID = os.getenv(
    "RAZORPAY_KEY_ID",
    "YOUR_RAZORPAY_KEY_ID"
)

RAZORPAY_KEY_SECRET = os.getenv(
    "RAZORPAY_KEY_SECRET",
    "YOUR_RAZORPAY_KEY_SECRET"
)


razorpay_client = razorpay.Client(
    auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET)
)


# =========================================================
# PAYMENT PAGE
# =========================================================
@payment_bp.route("/<int:booking_id>")
def payment_page(booking_id):

    # Demo booking amount
    amount = 500

    return render_template(
        "payment.html",
        booking_id=booking_id,
        amount=amount,
        razorpay_key=RAZORPAY_KEY_ID
    )


# =========================================================
# CREATE RAZORPAY ORDER
# =========================================================
@payment_bp.route("/create-order", methods=["POST"])
def create_order():

    booking_id = request.form.get("booking_id")
    amount = request.form.get("amount")

    try:

        amount = float(amount)

        # Razorpay amount is in paise
        amount_paise = int(amount * 100)

        order_data = {
            "amount": amount_paise,
            "currency": "INR",
            "payment_capture": 1
        }

        order = razorpay_client.order.create(
            data=order_data
        )

        return render_template(
            "payment.html",
            booking_id=booking_id,
            amount=amount,
            razorpay_key=RAZORPAY_KEY_ID,
            order_id=order["id"]
        )

    except Exception as e:

        print("Payment Error:", e)

        flash(
            "Unable to create payment order.",
            "danger"
        )

        return redirect(
            url_for(
                "payment.payment_page",
                booking_id=booking_id
            )
        )


# =========================================================
# PAYMENT SUCCESS
# =========================================================
@payment_bp.route("/success", methods=["POST"])
def payment_success():

    payment_id = request.form.get(
        "razorpay_payment_id"
    )

    order_id = request.form.get(
        "razorpay_order_id"
    )

    signature = request.form.get(
        "razorpay_signature"
    )

    booking_id = request.form.get(
        "booking_id"
    )

    try:

        # Verify Razorpay signature
        razorpay_client.utility.verify_payment_signature(
            {
                "razorpay_order_id": order_id,
                "razorpay_payment_id": payment_id,
                "razorpay_signature": signature
            }
        )

        # TODO:
        # Database માં payment details save કરો
        #
        # Payment(
        #     booking_id=booking_id,
        #     payment_id=payment_id,
        #     payment_status="Paid"
        # )

        return render_template(
            "payment-success.html",
            booking_id=booking_id,
            payment_id=payment_id
        )

    except Exception as e:

        print("Signature Verification Error:", e)

        return render_template(
            "payment-failed.html",
            booking_id=booking_id
        )


# =========================================================
# PAYMENT FAILED
# =========================================================
@payment_bp.route("/failed")
def payment_failed():

    booking_id = request.args.get(
        "booking_id"
    )

    return render_template(
        "payment-failed.html",
        booking_id=booking_id
    )