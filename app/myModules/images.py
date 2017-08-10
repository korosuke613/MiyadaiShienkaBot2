def open_image(cur) -> bool:
    row = cur.fetchone()
    if not row:
        return False

    pic = row[0]
    f = open('send_img.png', 'wb')
    f.write(pic)
    f.close()

    return True
