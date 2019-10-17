import unittest

import app


class HandleEmp:
    def add(self, session, username, mobile, workNumber):
        My_Date = {
            "username": username,
            "mobile": mobile,
            "workNumber": workNumber
        }
        return session.post(app.BG_URL + "user", json=My_Date, headers={"Authorization": "Bearer " + app.TOKEN})

    def get_emp(self, session):
        print("查询数据token: ", app.TOKEN)
        return session.get(app.BG_URL + "user/" + app.ID, headers={"Authorization": "Bearer " + app.TOKEN})

    def alter_emp(self, session, username1, mobile1):
        alter_emp = {
            "username": username1,
            "mobile": mobile1
        }
        return session.put(app.BG_URL + "user/" + app.ID, json=alter_emp,
                           headers={"Authorization": "Bearer " + app.TOKEN})

    def del_emp(self, session):
        return session.delete(app.BG_URL + "user/" + app.ID, headers={"Authorization": "Bearer " + app.TOKEN})
