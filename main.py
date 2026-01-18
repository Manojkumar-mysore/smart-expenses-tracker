
from database_config import DB_name,DB_host,DB_password,DB_user

import pymysql
# from database_config import DB_name,DB_host,DB_password,DB_user

def get_connection():
        connection = pymysql.connect(
                host = DB_host,
                user = DB_user,
                password = DB_password,
                database = DB_name
        )
        return connection

def add_income():
        connection = get_connection()
        cursor = connection.cursor()

        try:
                try :
                        month_number = int(input("enter month number(1-12): "))
                        if month_number < 1 or month_number > 12 :
                                print("month must be between 1-12 ")
                                return
                except ValueError:
                        print("month must be in number")
                        return

                try:
                    year = int(input("enter the year: "))
                    if year < 1 :
                        print("year must be greater then 0")
                        return
                except ValueError:
                    print("year must be in number")

                try:
                        income_amount = int(input("enter your monthly income: "))
                        if income_amount <= 0:
                                print("income must be greater than 0")
                                return
                except ValueError:
                        print("income amount must be in number")
                        return

                check_sql = """SELECT id FROM income_table where month_number = %s AND year = %s"""
                cursor.execute(check_sql,(month_number, year))
                existing = cursor.fetchone()

                # if data is existed
                if existing :

                        print("Income is already existing for this month and year \n")
                        print("1.update ")
                        print("2.cancel")

                        choice = input("choose on option (1 / 2):").strip()
                        if not choice:
                            print("you can't leave the choice blank")
                        if choice == "1":
                                update_sql = """UPDATE income_table SET income_amount = %s where month_number = %s AND year = %s"""
                                cursor.execute(update_sql,(income_amount, month_number, year))
                                connection.commit()
                                print("Income updated successfully \n")
                        else:
                            print("operation canceled \n")

                # if data is not existed
                else:
                    insert_sql = "INSERT INTO income_table (month_number,income_amount,year) VALUES (%s ,%s,%s)"
                    # values = (month_number, income_amount)
                    # cursor.execute(sql, values)
                    cursor.execute(insert_sql,(month_number, income_amount,year))
                    connection.commit()
                    print("income saved successfully \n")

        finally:
                cursor.close()
                connection.close()

def add_expenses():
        connection = get_connection()
        cursor = connection.cursor()

        try:
                category = input("enter category (food/grocery/clothes): ").strip()
                if not category:
                        print("category can't be empty" )
                        return

                item_name = input("enter the item name: ").strip()
                if not item_name:
                        print("item name can't be empty" )
                        return

                try:
                        amount = int(input("enter the item price: "))
                        if amount <= 0:
                                print("Amount should be grater than 0")
                                return
                except ValueError:
                        print("Amount must be in number")
                        return

                date = input("enter date (yyyy-mm-dd): ").strip()
                if not date:
                        print("date can't be empty")
                        return

                try:
                        year = int(input("enter the year: "))
                        if year < 1:
                                print("year must be greater then 0")
                                return
                except ValueError:
                        print("year must be in number")


                sql = "INSERT INTO expenses_table (category,item_name,amount,date,year) VALUES (%s, %s, %s, %s,%s)"
                values = (category, item_name, amount, date,year)
                cursor.execute(sql, values)
                connection.commit()
                print("expenses saved successfully \n")

        finally:
                cursor.close()
                connection.close()

def show_summary():
        connection= get_connection()
        cursor = connection.cursor()

        try:
                # month_name = input("enter the month name (ex:january): ").strip()
                # if not month_name:
                #         print("month name can't be empty")
                #         return

                try:
                        month = int(input("enter month number(1-12): "))
                        if (month < 1 or month  > 12) :
                                print("month number must be between 1 and 12")
                                return
                except ValueError:
                        print("month must be in number")
                        return

                try:
                        year = int(input("enter the year: "))
                        if year < 1:
                                print("year must be greater then 0")
                                return
                except ValueError:
                        print("year must be in number")

                # income
                cursor.execute("SELECT SUM(income_amount) from income_table WHERE month_number = %s AND year = %s",(month,year) )
                income = cursor.fetchone()

                # expenses
                cursor.execute("SELECT SUM(amount) from expenses_table WHERE MONTH(date) =%s AND year = %s",(month,year))
                expenses = cursor.fetchone()

                income_values = income[0] if income and income[0] is not None else 0
                expenses_values = expenses[0] if expenses and expenses[0] is not None else 0
                remaining = income_values - expenses_values

                print("\n----monthly summary-----")
                print("income    :",income_values)
                print("expenses  :",expenses_values)
                print("remaining :",remaining)
                print()
        finally:
                cursor.close()
                connection.close()

def main():
        while True:
                print("\t  ----welcome----")
                print("1.ADD INCOME")
                print("2.ADD EXPENSES")
                print("3.SHOW SUMMARY")
                print("4.EXIT")

                choice = input("choose on option :").strip()
                if not choice:
                    print("you can't leave the choice blank")
                    continue
                if choice == "1":
                    add_income()
                elif choice == "2":
                    add_expenses()
                elif choice == "3":
                    show_summary()
                elif choice == "4":
                    print("thank you")
                    break
                else:
                    print("invalid input choose 1-4")


if __name__=="__main__":
        main()
