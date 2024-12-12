from flask import Blueprint, session, redirect, url_for
from user.views.user_view import (
    list_users_view,
    create_user_view,
    login_user_view,
    user_dashboard_view
)

user_bp = Blueprint(
    "user_bp", __name__, template_folder="templates", static_folder="static"
)


@user_bp.route("/")
def home():
    return redirect(url_for("user_bp.login"))


def substring_after(s, delim):
    return s.partition(delim)[1]


@user_bp.route("/list")
def users():
    return list_users_view()


@user_bp.route("/create", methods=["GET", "POST"])
def create_user():
    return create_user_view()


@user_bp.route("/login", methods=["GET", "POST"])
def login():
    return login_user_view()


@user_bp.route("/logout")
def logout():
    session.pop("logged_in", None)
    session.pop("name", None)
    return redirect(url_for("user_bp.login"))


@user_bp.route("/dashboard")
def dashboard():
    return user_dashboard_view()
