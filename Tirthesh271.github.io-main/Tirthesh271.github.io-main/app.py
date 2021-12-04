import pymysql
from flask import Flask, render_template, request
app = Flask(__name__)

def TupList(tup, lis):
    #print(tup)
    for i in tup:
        #print(i)
        lis.append(i)
    return lis

@app.route('/')
def student():
   return render_template('login.html')

@app.route('/result',methods = ['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        result = request.form.to_dict()
        print('Form data', result)
        #print(result['Name'])
        select = 0

        host = 'localhost'
        user = 'root'
        password = 'Rajgad@12'
        db = 'ezzycar'

        final = []

        try:
            con = pymysql.connect(host=host, user=user, password=password, db=db, use_unicode=True, charset='utf8')
            print('+=========================+')
            print('|  CONNECTED TO DATABASE  |')
            print('+=========================+')
        except Exception as e:
            print("error")
        cur = con.cursor()
        cur.execute("SELECT * FROM carspecification ")
        data = cur.fetchall()
        #print(data)
        print(data[0][0])
        print("debug")
        for i in data:
            print(i)

        if(int(result['Name']) == int(data[0][0]) and result['Password'] == data[0][1]):
            final = TupList(data[select], final)

            cur.execute("SELECT * FROM carcare ")
            data = cur.fetchall()
            final = TupList(data[select], final)

            cur.execute("SELECT * FROM cardocuments ")
            data = cur.fetchall()
            final = TupList(data[select], final)

            cur.execute("SELECT * FROM carmaintenance ")
            data = cur.fetchall()
            final = TupList(data[select], final)

            data = tuple(final)
            di = {'info': data}
            print(data)
            print(di)
            #print(data[select])#check username here and select appropriate index

            return render_template('index.html',data = di)

        else:
            return render_template('err.html')

        if (int(result['Name']) == int(data[1][0]) and result['Password'] == data[1][1]):
            select=1
            final = TupList(data[select], final)

            cur.execute("SELECT * FROM carcare ")
            data = cur.fetchall()
            final = TupList(data[select], final)

            cur.execute("SELECT * FROM cardocuments ")
            data = cur.fetchall()
            final = TupList(data[select], final)

            cur.execute("SELECT * FROM carmaintenance ")
            data = cur.fetchall()
            final = TupList(data[select], final)

            data = tuple(final)
            di = {'info': data}
            print(data)
            print(di)
            # print(data[select])#check username here and select appropriate index

            return render_template('index.html', data=di)

        else:
            return render_template('err.html')
if __name__ == '__main__':
   app.run()
