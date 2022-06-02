#
#
#
# Working with CSV Files
#     1.If any file is saved .csv called CSV File
#     2.CSV means Comm Sep Values.
#
# Steps For Writing Data into CSV File :
#     1.open the file in write mode
#        Eg:  f=open("mystu.csv","w")
#
#     2.create csv_writer class object by using
#           writer(file) -> csvwriter class object
#           from csv module.
#              cwriter=csv.writer(f)
#
#     3.Inorder to write the data into csv file, we have
#     to use writerow(iterable) from csvwriter class.
#                   cwriter.writerow(["sno","sname","scity"])
#
# Steps for Reading Data From CSV File:
#     1.open the file in read mode.
#         f=open("stu3.csv","r")
#
#     2.create csv_reader object
#             reader(file) -> cscreader object
#                cro=csv.reader(f)
#
#     Note: cro object is the collection of List items
#     cro object is an iterable
#
#
#
#
#
