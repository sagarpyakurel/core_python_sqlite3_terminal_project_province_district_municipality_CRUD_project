import sqlite3


class DBHelper:

    def __init__(self):

        self.con = sqlite3.connect('mydatabase.db')
        print('\n##### database connected successfully #####')
        cursor = self.con.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")
        query = 'create table if not exists province(p_id integer primary key autoincrement, p_name varchar(100) unique)'
        cursor.execute(query)
        print("******** created table Province ******** ")

        query = 'create table if not exists district(d_id integer primary key autoincrement, d_name varchar(100),F_pid,FOREIGN KEY(F_pid) REFERENCES province(p_id) on delete cascade)'
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.execute(query)
        print("********* created table District *******")

        query = 'create table if not exists municipality(m_id integer primary key autoincrement, m_name varchar(100),F_did,FOREIGN KEY(F_did) REFERENCES district(d_id) on delete cascade)'
        cursor.execute(query)
        print("******** created table municipality *******")

# insert province
    def insert_province(self, province_name):
        query = f"insert into province(p_name)values('{province_name}')"
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("province name is saved")


# insert district
    def fetchprovince_insertdistrict(self, district_name, province_name):
        query = f"select p_id from province where p_name='{province_name}'"
        cursor = self.con.cursor()
        cursor.execute(query)
        for province in cursor:
            p_id = province[0]
        query = f"insert into district(d_name,F_pid) values('{district_name}','{p_id}')"
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print(f"district:{district_name} successfully inserted")

    def fetchdistrict_insertmunicipality(self, municipality_name, district_name):
        query = f"select d_id from district where d_name='{district_name}'"
        cursor = self.con.cursor()
        cursor.execute(query)
        for district in cursor:
            d_id = district[0]
        query = f"insert into municipality(m_name,F_did) values('{municipality_name}','{d_id}')"
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print(f"municipality:{municipality_name} successfully inserted")

        # print('p_id:', province['p_id'])

    #  fetch all province
    def fetchallprovince(self):
        query = "select * from province"
        cursor = self.con.cursor()
        cursor.execute(query)
        for province in cursor:
            print(province[1], "\t")

     # fetch all district
    def fetchalldistrict(self):
        query = "select * from district"
        cursor = self.con.cursor()
        cursor.execute(query)
        for district in cursor:
            print(district[1], "\t")

    # fetch all municipality
    def fetchallmunicipality(self):
        query = "select * from municipality"
        cursor = self.con.cursor()
        cursor.execute(query)
        for municipality in cursor:
            print(municipality[1], "\t")

    def getallprovince(self):
        query = "select * from province"
        cursor = self.con.cursor()
        cursor.execute(query)
        return [provience[1] for provience in cursor]

    def getalldistrict(self):
        query = "select * from district"
        cursor = self.con.cursor()
        cursor.execute(query)
        return [district[1] for district in cursor]

    def getallmunicipality(self):
        query = "select * from municipality"
        cursor = self.con.cursor()
        cursor.execute(query)
        return [municipality[1] for municipality in cursor]

    def getprovincedictionary(self):
        query = "select * from province"
        cursor = self.con.cursor()
        cursor.execute(query)
        # for province in cursor:
        return [provience for provience in cursor]
        # return cursor

    def fetch_province(self, name):
        query = f"select * from province where p_name='{name}'"
        cursor = self.con.cursor()
        cursor.execute(query)

        for province in cursor:
            print('p_name:', province['name'])

    def delete_province(self, inputname):
        query = f"delete from province where p_name='{inputname}'"
        print(query)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print(f"\n province name:{inputname} deleted")

    def delete_district(self, inputname):
        query = f"delete from district where d_name='{inputname}'"
        print(query)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print(f"\n district name:{inputname} deleted")

    def delete_municipality(self, inputname):
        query = f"delete from municipality where m_name='{inputname}'"
        print(query)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print(f"\n municipality name:{inputname} deleted")


# update province
    def update_province(self, oldname, newname):
        query = f"update province set p_name='{newname}' where p_name='{oldname}'"
        # print(query)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("province name updated successfully")

# update district
    def update_district(self, oldname, newname):
        query = f"update district set d_name='{newname}' where d_name='{oldname}'"
        # print(query)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print("district name updated successfully")

    def update_municipality(self, oldname, newname):
        query = f"update municipality set m_name='{newname}' where m_name='{oldname}'"
        # print(query)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print(f"municipality name:{newname} updated successfully")

    def listdistrict_by_province(self, province_name):
        query = f"select p_id from province where p_name='{province_name}'"
        cursor = self.con.cursor()  
        cursor.execute(query)
        for province in cursor:
            p_id = province[0]  
        query = f"select d_name from district where F_pid='{p_id}'"   
        cursor = self.con.cursor()
        cursor.execute(query)
        for district in cursor:
            print(district[0])
      
    def listmunicipality_by_district(self,district_name):
        query = f"select d_id from district where d_name='{district_name}'"
        cursor = self.con.cursor()  
        cursor.execute(query)
        for district in cursor:
            d_id = district[0]  
        query = f"select m_name from municipality where F_did='{d_id}'"   
        cursor = self.con.cursor()
        cursor.execute(query)
        for municipality in cursor:
            print(municipality[0])


# def getdistrictname(self, provincename):
#  query =f"select name from district where p_id='20'"
#  starting work with district
#  starting work with district
#  starting work with district
#  starting work with district

# making constructor of DBHelper class this will connect db and create table
# helper = DBHelper()
# helper.insert_province("province-1")
# helper.insert_province("province-5")
# helper.fetch_province('bagmati')
# helper.delete_province(500)
# helper.update_province('newprovince', 'provincenew1')
# helper.fetchallprovince()
 