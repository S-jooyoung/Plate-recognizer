import pymysql


def connect(num, chars):

    db_addr = pymysql.connect(
        user='',
        passwd='',
        host='',
        db='',
        charset=''
    )

    s_num = num
    cursor = db_addr.cursor(pymysql.cursors.DictCursor)

    insert = "insert into parkin_info(car_num,ent_date,img_name) values (%s,now(),%s)"
    car_num = chars
    img_name = 'frame%d.jpg' % s_num
    cursor.execute(insert, (car_num, img_name))
    db_addr.commit()

    result = cursor.fetchall()
    result
