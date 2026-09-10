@admin_bp.route('/admin/assign-roles',methods=['GET', 'POST'])
@login_required
def assign_roles():
#GET  when an admin first visits the page, they need to see the form: a list of users and a dropdown to pick roles. That’s a GET request just show me the page content.
    # Only super admin can access
    if current_user.role != "admin":
        return redirect(url_for("student.dashboard"))
    # Only super admin can access this page
    if not current_user.is_super_admin:
        flash("Access denied.", "danger")
        return redirect(url_for("admin.dashboard"))
#POST, when the admin actually submits the form (picks a user and a new role, clicks “Update”), that’s a POST “here’s data, do something with it.” That’s exactly what this blockdoes...
    if request.method == "POST":
        user_id = request.form.get("user_id")
        new_role = request.form.get("role")

        user = User.query.get(user_id)

        # 🚫 Prevent changing super admin role
        if user.is_super_admin:
                flash("You cannot change the Super Admin role.", "danger")
                return redirect(url_for("admin.assign_roles"))

        if user:
            user.role = new_role
            db.session.commit()
            flash("Role updated successfully!", "success")

        return redirect(url_for("admin.assign_roles"))
#This only runs when it’s a GET request (because the if request.method == "POST": block above it didn’t match, so Python falls through to this).
    users = User.query.all()
    return render_template("assign_roles.html", users=users)

tried to visit a protected page directly after session timeout, i was redirected to login page..