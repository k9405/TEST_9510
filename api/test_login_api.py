import app


class LoginApi:

    def loginapi(self, session, mobile, password):
        my_date = {"mobile": mobile,
                   "password": password
                   }
        return session.post(app.BG_URL + "login", json=my_date)
