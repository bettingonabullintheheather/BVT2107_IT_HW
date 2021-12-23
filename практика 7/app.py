import psycopg2
import sys
from PyQt5.QtWidgets import (QApplication, QWidget,QTabWidget, QAbstractScrollArea,QVBoxLayout, QHBoxLayout,QTableWidget, QGroupBox,QTableWidgetItem, QPushButton, QMessageBox)
from PyQt5.QtGui import QBrush, QColor
import datetime
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.days = []
        self._connect_to_db()
        self.setWindowTitle("schedule")
        self.vbox = QVBoxLayout(self)
        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)
        self._create_schedule_tab("Monday")
        self._create_schedule_tab("Tuesday")
        self._create_schedule_tab("Wednesday")
        self._create_schedule_tab("Thursday")
        self._create_schedule_tab("Friday")
        self._create_schedule_tab("Saturday")


    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="another",
                        user="postgres",
                        password="21082003",
                        host="localhost",
                        port="5432")
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
    
   
    def _create_schedule_tab(self,dayName):
        schedule_tab = QWidget()
        self.tabs.addTab(schedule_tab, "schedule " + dayName)
        self.monday_gbox = QGroupBox(dayName)
        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        self.shbox1.addWidget(self.monday_gbox)
        table = self._create_day_table(dayName)
        self.update_schedule_button = QPushButton("Update")
        self.add_schedule_button = QPushButton("Add")
        self.shbox2.addWidget(self.update_schedule_button)
        self.shbox2.addWidget(self.add_schedule_button)
        self.add_schedule_button.clicked.connect(lambda:self._add_line_table(dayName,table))
        self.update_schedule_button.clicked.connect(lambda:self._update_day_table(dayName,table))
        schedule_tab.setLayout(self.svbox)
   
   
    def _create_day_table(self,day):
        table = QTableWidget()
        self.days.append(table)
        table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["Subject","Time", "", ""])
        self._update_day_table(day,table)
        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(table)
        self.monday_gbox.setLayout(self.mvbox)
        return table
  
  
    def _add_line_table(self,dayName,table):
        table.setRowCount(table.rowCount()+1);
        table.setItem(table.rowCount()-1, 1,QTableWidgetItem("Время начала"))
        table.setItem(table.rowCount()-1, 0,QTableWidgetItem("Название предмета"))
        table.setItem(table.rowCount()-1, 2,QTableWidgetItem("ODD/EVEN/ALWAYS"))
        joinButton = QPushButton("Join")

        table.setCellWidget(table.rowCount()-1, 3, joinButton)
        joinButton.clicked.connect(lambda:self.add_line(table.rowCount()-1,table,dayName))
    
    
    def _update_day_table(self,day,table):

        self.cursor.execute("SELECT * FROM schedule.schedule WHERE (frequency=%s OR frequency IS NULL OR frequency='' OR frequency='ALWAYS') AND day=%s ORDER BY start_time",(GetWeek(),day.upper()))
        records = list(self.cursor.fetchall())
        table.setRowCount(len(records))
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            dropButton = QPushButton("Delete")
            id = QTableWidgetItem(str(r[0]))
            id.setForeground(QBrush(QColor(0, 255, 0)))

            table.setItem(i, 0,QTableWidgetItem(str(r[2])))
            table.setItem(i, 1,QTableWidgetItem(str(r[1])))
            table.setItem(i, 4,id)
            table.setCellWidget(i, 3,dropButton)
            table.setCellWidget(i, 2, joinButton)

            def get_change_method(ind,id):
                return lambda:self._change_day_from_table(ind,day,table,id)
            def get_del_method(ind,id):
                return lambda:self._delete_row(ind,table,id)

            joinButton.clicked.connect(get_change_method(i,str(r[0])))
            dropButton.clicked.connect(get_del_method(i,str(r[0])))
        table.resizeRowsToContents()
   
   
    def _change_day_from_table(self, rowNum, day,table,subject_id):
        row = list()
        lasttime = 0
        for i in range(table.columnCount()):
            try:
                row.append(table.item(rowNum,i).text())
            except:
                row.append(None)

        try:
            self.cursor.execute("UPDATE schedule.schedule SET subject=%s WHERE id = %s", (row[0],subject_id))
            self.cursor.execute("UPDATE schedule.schedule SET start_time=%s WHERE id = %s", (row[1],subject_id))
        except:
            QMessageBox.about(self, "Error", "Enter all fields")
   
   
    def _delete_row(self,rowNum,table,id):
        try:
            self.cursor.execute("SELECT * FROM schedule.schedule WHERE id=%s",(id,))
            day = list(self.cursor.fetchall())[0][3]
            self.cursor.execute("DELETE FROM schedule.schedule WHERE id = %s", (id,))
            self._update_day_table(day,table)
            
        except:
            QMessageBox.about(self, "Error", "Can't delete")
        pass
    def add_line(self,i,table,dayName):
        time = table.item(i,1).text()
        name = table.item(i,0).text()
        freq = table.item(i,2).text()
        self.cursor.execute("INSERT INTO schedule.schedule (start_time,subject,day,frequency) VALUES (%s,%s,%s,%s)",(time,name,dayName.upper(),freq))


def GetWeek():
    year = datetime.datetime.now().year
    firstSept = datetime.datetime(year,9,1).isocalendar().week
    currentWeek = datetime.datetime.now().isocalendar().week - firstSept+1
    return str('ODD') if currentWeek % 2 else str('EVEN')


app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())