

def test_signup_new_account(app):
    username = "root"
    password = "root"
    app.james.ensure_user_exist(username, password)