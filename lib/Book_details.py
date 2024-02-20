def add_book():
    import mysql.connector as Book
    Book=Book.connect(host="localhost",user="root",password="4568",database="12_project")
    Bcursor=Book.cursor( )
    print("*"*60)
    Book_id=int(input("Enter Book Id:"))
    Book_Name=input("Enter Book Name:")
    Author_Name=input("Enter Name Of The Author:")
    Quantity=int(input("Enter Quantity Of The Book:"))
    Genre=input("Enter Genre Of The Book:")
    Record=(Book_id,Book_Name,Author_Name,Quantity,Genre)
    Bcursor.execute("Select * from Quest_Library")
    R=Bcursor.fetchall()
    for i in R:
        if i[1]==Record[1] and i[2]==Record[2]:
            E="Update Quest_Library set Quantity={} where Book_id='{}'".format(i[3]+Quantity,i[0])
            Bcursor.execute(E)
            Book.commit()
            print("BOOK ADDED TO THE PREVIOUS STACK")
            break
    else:
        A=("insert into Quest_Library values ('{}','{}','{}','{}','{}')").format(Book_id,Book_Name,Author_Name,Quantity,Genre)
        Bcursor.execute(A)
        Book.commit()
        print("NEW BOOK ADDED")
        print("*"*50)

def display_books():
    import mysql.connector as Book
    Book=Book.connect(host="localhost",user="root",password="4568",database="12_project")
    Bcursor=Book.cursor( )
    print("Book_id,Book_Name,Author_Name,Quantity,Genre")
    Bcursor.execute("Select * from Quest_Library")
    J=Bcursor.fetchall()
    for i in J:
        print(i)
    print("*"*80)

def delete_book():
    import mysql.connector as Book
    Book=Book.connect(host="localhost",user="root",password="4568",database="12_project")
    Bcursor=Book.cursor( )
    print("*"*80)
    print("1.Book Name")
    print("2.Book Id")
    print("_"*50)
    C=int(input("Enter You Choice:"))
    if C==1:
        N=input("Enter the Book Name Which You Want to Delete:")
        Y="Delete from Quest_Library where (Book_Name='{}')".format(N)
        Bcursor.execute(Y)
        Book.commit()
    elif C==2:
        N=input("Enter the Book's I'd Which You Want to Delete:")
        Y='Delete from Quest_Library where Book_id="{}"'.format(N)
        Bcursor.execute(Y)
        Book.commit()
    else:
        print("****WRONG INPUT****")
    print("Deleted")
    print("*"*30)
def update_book():
    import mysql.connector as Book
    Book=Book.connect(host="localhost",user="root",password="4568",database="12_project")
    Bcursor=Book.cursor( )
    print("-"*50)
    print("***OPTIONS FOR MODIFICATION***")
    print("1. Book Id")
    print("2. Book Name")
    print("3. Author Name")
    print("4. Book Quantity")
    C1=input("Enter Your Choice From The Menu Which You Want To Modify:")
    C2=input("Enter Option To Be Changed On The Basis Of:")
    if C1=='1':
        if C2=='1':
            A=input("Enter Book Id To Be Added:")
            B=input("Enter Book Id To Be Removed:")
            Y='update Quest_Library set Book_id="{}" where Book_id="{}"'.format(A,B)
        elif C2=='2':
            A=input("Enter Book Id To Be Added:")
            B=input("Enter Book Name Whose Id Is To Be Removed:")
            Y="update Quest_Library set Book_id='{}' where Book_Name='{}'".format(A,B)
        elif C2=='3':
            A=input("Enter Book Id To Be Added:")
            B=input("Enter Author Name Whose Id Is To Be Removed:")
            Y="(update Quest_Library set Book_id='{}' where Author_Name='{}')".format(A,B)
        elif C2=='4':
            A=input("Enter Book Id To Be Added:")
            B=input("Enter Quantity of Book Whose Id Is To Be Removed:")
            Y="(update Quest_Library set Book_id='{}' where Quantity='{}')".format(A,B)
    elif C1=='2':
        if C2=='1':
            A=input("Book Name To Be Changed To")
            B=input("Book Id On The Basis Of Which Name To Be Changed:")
            Y="(update Quest_Library set Book_Name='{}' where Book_id='{}')".format(A,B)
        elif C2=='2':
            A=input("Book Name To Be Changed To")
            B=input("Book Name On The Basis Of Which Name To Be Changed:")
            Y="(update Quest_Library set Book_Name='{}' where Book_Name='{}')".format(A,B)
        elif C2=='3':
            A=input("Book Name To Be Changed To")
            B=input("Book Author Name On The Basis Of Which Name To Be Changed:")
            Y="(update Quest_Library set Book_Name='{}'where Book_Author='{}')".format(A,B)
        elif C2=='4':
            A=input("Book Name To Be Changed To")
            B=input("Book Quantity On The Basis Of Which Name To Be Changed:")
            Y="(update Quest_Library set Book_Name='{}' where Quantity='{}')".format(A,B)
    elif C1=='3':
        if C2=='1':
            A=input("Author Name To Be Changed To")
            B=input("Book Id On The Basis Of Which Author Name To Be Changed:")
            Y="(update Quest_Library set Author_Name='{}' where Book_id='{}')".format(A,B)
        elif C2=='2':
            A=input("Author Name To Be Changed To")
            B=input("Book Name On The Basis Of Which Author Name To Be Changed:")
            Y="(update Quest_Library set Author_Name='{}' where Book_Name='{}')".format(A,B)
        elif C2=='3':
            A=input("Author Name To Be Changed To")
            B=input("Book Author Name On The Basis Of Which Author Name To Be Changed:")
            Y="(update Quest_Library set Author_Name='{}' where Book_Author='{}')".format(A,B)
        elif C2=='4':
            A=input("Author Name To Be Changed To")
            B=input("Book Quantity On The Basis Of Which Author Name To Be Changed:")
            Y="(update Quest_Library set Author_Name='{}' where Quantity='{}')".format(A,B)
    elif C1=='4':
        if C2=='1':
            A=input("Book Quantity To Be Changed To")
            B=input("Book Id On The Basis Of Which Quantity To Be Changed:")
            Y="(update Quest_Library set Quantity='{}' where Book_id='{}')".format(A,B)
        elif C2=='2':
            A=input("Book Quantity To Be Changed To")
            B=input("Book Name On The Basis Of Which Quantity To Be Changed:")
            Y="(update Quest_Library set Quantity='{}' where Book_Name='{}')".format(A,B)
        elif C2=='3':
            A=input("Book Quantity To Be Changed To")
            B=input("Book Author Name On The Basis Of Which Quantity  To Be Changed:")
            Y="(update Quest_Library set Quantity='{}' where Book_Author='{}')".format(A,B)
        elif C2=='4':
            A=input("Book Quantity To Be Changed To")
            B=input("Book Quantity On The Basis Of Which Quantity  To Be Changed:")
            Y="(update Quest_Library set Quantity='{}' where Quantity='{}')".format(A,B)
    print("Data Modified")
    
def Search_book():
    import mysql.connector as Book
    Book=Book.connect(host="localhost",user="root",password="4568",database="12_project")
    Bcursor=Book.cursor( )
    Q="Select * from Quest_Library"
    Bcursor.execute(Q)
    for i in Bcursor:
        i=list(i)
    print("*"*55)
    print("***OPTIONS FOR SEARCHING***")
    print("1. Book Id")
    print("2. Book Name")
    print("3. Author Name")
    print("\n")
    C4=input("Enter A Choice:")
    if C4=='1':
        P=input("Enter The Book Id To Be Searched:")
        if i[0]==P:
            Y="Select * from Quest_Library Where Book_id='{}'".format(P)
            Bcursor.execute(Y)
            K=Bcursor.fetchall()
            print(K)
        else:
            print("***Id Not Found***")
    elif C4=='2':
        P=input("Enter The Book NameTo Be Searched:")
        if i[1]==P:
            Y="Select * from Quest_Library Where Book_Name='{}'".format(P)
            Bcursor.execute(Y)
            K=Bcursor.fetchall()
            print(K)
        else: 
            print("***Book Name Not Found***")        
    elif C4=='3':
        P=input("Enter The Author NameTo Be Searched:")
        if i[2]==P:
            Y="Select * from Quest_Library Where Author_Name='{}'".format(P)
            Bcursor.execute(Y)
            K=Bcursor.fetchall()
            print(K)
        else:
            print("***Author Name Not Found***")



 
Search_book()
