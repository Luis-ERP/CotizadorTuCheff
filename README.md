# CotizadorTuCheff

Complex price quote generator using Python and PyQT5, a technology to create GUI interfaces. 
Thist is the most complex project I've done. I actually recently remade this project so it 
could be more efficient and applied knowledge I've gathered working with Android apps with
Android Studio. The app has several functionalities, it generates a PDF file with all the
information passed by the user. I also gives the option to user of storing templates of pre-
gathered information so the process of creating a price quote is easier and faster.

Here was of extreme importance the structure of project, as I had python files for UI/UIX 
interface, the logic scripts, and the databases connections. Because of it's complexity, 
I had to borrow the concept of MVC from web development.

For databases, as the client wanted the information to be accessible from different devices,
I integrated a real time database of Firebase, a storage service provided by Google. I did like
it, since it was a not relational database, I had the freedom to manage data more efficient,
otherwise I couldn't have done it with SQL.

To generate the PDF I used ReportLab, a Python library to write in PDF formats. It was my first
time working with it. Even tho, it was hard for me, I was able to pull it of as well.

Requirements
* Python 3.7.X 
* PyQt5
* Pyrebase4
* Python-firebase
* Reportlab

To run, execute  CotizadorTuCheff.py
