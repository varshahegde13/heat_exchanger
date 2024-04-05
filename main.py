import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator, QPixmap, QColor, QLinearGradient, QPalette, QBrush
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QVBoxLayout, QGridLayout, \
    QFormLayout, QLineEdit, QPushButton, QGroupBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class LogoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.showMaximized()
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor(255, 255, 255))
        gradient.setColorAt(0.0, QColor(230, 230, 250))

        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(gradient))
        self.setPalette(palette)

        # Header
        self.MainLayout = QGridLayout()
        self.setLayout(self.MainLayout)

        self.logo_label = QLabel()
        self.logo_label.setPixmap(QPixmap("logo.png").scaledToWidth(150))
        self.MainLayout.addWidget(self.logo_label, 0, 0, 1, 1)

        self.h_label = QLabel("Heat Exchanger Design and Analysis")
        self.h_label.setStyleSheet("border: 2px solid black; color: black; font-size: 50px;")
        self.h_label.setAlignment(Qt.AlignCenter)
        self.MainLayout.addWidget(self.h_label, 0, 0, 1, 13)

        # Buttons
        self.model_button = QPushButton("Model")
        self.model_button.setStyleSheet("font-size: 50px;")
        self.model_button.setFixedSize(500, 100)
        self.MainLayout.addWidget(self.model_button, 1, 0, 3, 3)

        self.graph_button = QPushButton("Graph")
        self.graph_button.setStyleSheet("font-size: 50px;")
        self.graph_button.setFixedSize(500, 100)
        self.MainLayout.addWidget(self.graph_button, 3, 0, 3, 3 )

        self.draw_button = QPushButton("Draw")
        self.draw_button.setStyleSheet("font-size: 50px;")
        self.draw_button.setFixedSize(500, 100)
        self.MainLayout.addWidget(self.draw_button, 5, 0, 3, 3 )

        self.ppt_button = QPushButton("PPT")
        self.ppt_button.setStyleSheet("font-size: 50px;")
        self.ppt_button.setFixedSize(500, 100)
        self.MainLayout.addWidget(self.ppt_button, 1, 10, 3, 3)

        self.options_button = QPushButton("Options")
        self.options_button.setStyleSheet("font-size: 50px;")
        self.options_button.setFixedSize(500, 100)
        self.MainLayout.addWidget(self.options_button, 4, 10, 3, 3)

        # Graph
        self.graphWidget1 = plt.figure()
        # self.ax = self.graphWidget1.add_subplot(111)
        self.canvas = FigureCanvas(self.graphWidget1)

        self.graphWidget = QWidget()
        self.graph1Layout = QVBoxLayout(self.graphWidget)
        # self.graphWidget1.patch.set_facecolor('lightgreen')
        self.graph1Layout.addWidget(self.canvas)
        self.MainLayout.addWidget(self.graphWidget, 1, 3, 7, 7)

        # play button
        previous_button = QPushButton('◄', self)
        next_button = QPushButton('►', self)
        self.play_layout = QHBoxLayout()
        self.play_layout.addWidget(previous_button)
        self.play_layout.addWidget(next_button)
        play_button_widget = QWidget()
        play_button_widget.setLayout(self.play_layout)
        self.MainLayout.addWidget(play_button_widget, 8, 3, 1, 7)

        # Input
        self.inputLayout = QFormLayout()
        self.userinput = QLabel("User Inputs", self)
        self.userinput.setAlignment(Qt.AlignCenter)
        self.userinput.setStyleSheet("font-size: 20px; color: green; border: 2px solid black;")
        self.inputLayout.addRow(self.userinput)
        self.MainLayout.addLayout(self.inputLayout, 10, 0, 2, 6)

        #input forms
        self.rehot_input = QLineEdit("")
        self.rehot_input.setPlaceholderText("Rehot")
        self.rehot_input.setFixedSize(200,40)
        self.MainLayout.addWidget(self.rehot_input,10,0,3,5)

        self.input3 = QLineEdit()
        self.input3.setPlaceholderText("input3")
        self.input3.setFixedSize(200, 40)
        self.MainLayout.addWidget(self.input3, 10, 2, 3, 5)

        self.input2 = QLineEdit()
        self.input2.setPlaceholderText("input2")
        self.input2.setFixedSize(200, 40)
        self.MainLayout.addWidget(self.input2,11,0,3,5)

        self.input4 = QLineEdit()
        self.input4.setPlaceholderText("input4")
        self.input4.setFixedSize(200, 40)
        self.MainLayout.addWidget(self.input4, 11, 2, 3, 5)

        self.input5 = QLineEdit()
        self.input5.setPlaceholderText("input5")
        self.input5.setFixedSize(200, 40)
        self.MainLayout.addWidget(self.input5, 10, 4, 3, 5)

        self.input6 = QLineEdit("")
        self.input6.setPlaceholderText("input6")
        self.input6.setFixedSize(200, 40)
        self.MainLayout.addWidget(self.input6, 11, 4, 3, 5)


        self.allinput_button = QPushButton("All Input")
        self.allinput_button.setStyleSheet("font-size: 20px;")
        self.allinput_button.setFixedSize(150, 50)
        self.MainLayout.addWidget(self.allinput_button, 12, 2, 3, 3)

        #user output
        self.outputLayout = QFormLayout()
        self.useroutput = QLabel("User Output", self)
        self.useroutput.setAlignment(Qt.AlignCenter)
        self.useroutput.setStyleSheet("font-size: 20px; color: green; border: 2px solid black;")
        self.outputLayout.addRow(self.useroutput)
        self.MainLayout.addLayout(self.outputLayout, 10, 6, 2, 7)

        self.output1 = QLineEdit()
        self.output1.setPlaceholderText("output1")
        self.output1.setFixedSize(200, 40)
        self.MainLayout.addWidget(self.output1, 10, 6, 3, 5)

        self.output2 = QLineEdit()
        self.output2.setPlaceholderText("output2")
        self.output2.setFixedSize(200, 40)
        self.MainLayout.addWidget(self.output2, 10, 8, 3, 5)

        # new window for all input

        self.allinput_button.clicked.connect(self.openAllInputWindow)
    def openAllInputWindow(self):
        self.all_input_window = AllInputWindow()
        self.all_input_window.show()
class AllInputWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.MainLayout = QGridLayout()
        self.setLayout(self.MainLayout)

        # self.setFixedSize(1000, 2000)
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor(255, 255, 255))
        gradient.setColorAt(1.0, QColor(135, 206, 250))

        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(gradient))
        self.setPalette(palette)

        # all 24 inputs in forms

        self.rehot_input = QLineEdit("")
        self.rehot_input.setPlaceholderText("Rehot")
        self.rehot_input.setFixedSize(280, 70)
        self.MainLayout.addWidget(self.rehot_input, 0, 5, 3, 5)

        self.recold = QLineEdit("")
        self.recold.setPlaceholderText("recold")
        self.recold.setFixedSize(280, 70)
        self.MainLayout.addWidget(self.recold, 0, 10, 3, 5)

        self.t_hot_input = QLineEdit("")
        self.t_hot_input.setPlaceholderText("T_hot_in")
        self.t_hot_input.setFixedSize(280, 70)
        self.MainLayout.addWidget(self.t_hot_input, 0, 15, 3, 5)

        self.t_cold = QLineEdit("")
        self.t_cold.setPlaceholderText("T_cold_in")
        self.t_cold.setFixedSize(280, 70)
        self.MainLayout.addWidget(self.t_cold, 0, 20, 3, 5)

        self.p_hot = QLineEdit("")
        self.p_hot.setPlaceholderText("P_hot_in")
        self.p_hot.setFixedSize(280, 70)
        self.MainLayout.addWidget(self.p_hot, 0, 29, 3, 5)

        self.p_cold = QLineEdit("")
        self.p_cold.setPlaceholderText("P_cold_in")
        self.p_cold.setFixedSize(280, 70)
        self.MainLayout.addWidget(self.p_cold, 1, 29, 3, 5)

        self.t_input = QLineEdit("")
        self.t_input.setPlaceholderText("t")
        self.t_input.setFixedSize(280, 70)
        self.MainLayout.addWidget(self.t_input, 1, 20, 3, 5)

        self.w_input = QLineEdit("")
        self.w_input.setPlaceholderText("w")
        self.w_input.setFixedSize(280, 70)
        self.MainLayout.addWidget(self.w_input, 1, 15, 3, 5)

        self.b_input = QLineEdit("")
        self.b_input.setPlaceholderText("b")
        self.b_input.setFixedSize(280, 70)
        self.MainLayout.addWidget(self.b_input, 1, 10, 3, 5)

        self.h_input = QLineEdit("")
        self.h_input.setPlaceholderText("h")
        self.h_input.setFixedSize(280, 70)
        self.MainLayout.addWidget(self.h_input, 1, 5, 3, 5)

        self.l_input = QLineEdit("")
        self.l_input.setPlaceholderText("L")
        self.l_input.setFixedSize(280, 70)
        self.MainLayout.addWidget(self.l_input, 1, 5, 3, 5)

        self.a_input = QLineEdit("")
        self.a_input.setPlaceholderText("A")
        self.a_input.setFixedSize(280, 70)
        self.MainLayout.addWidget(self.a_input, 1, 10, 3, 5)

        self.lmba_input = QLineEdit("")
        self.lmba_input.setPlaceholderText("lmba")
        self.lmba_input.setFixedSize(280, 70)
        self.MainLayout.addWidget(self.lmba_input, 1, 15, 3, 5)

        self.tz_input = QLineEdit("")
        self.tz_input.setPlaceholderText("tz")
        self.tz_input.setFixedSize(280, 70)
        self.MainLayout.addWidget(self.tz_input, 1, 20, 3, 5)

        self.ty_input = QLineEdit("")
        self.ty_input.setPlaceholderText("ty")
        self.ty_input.setFixedSize(280, 70)
        self.MainLayout.addWidget(self.ty_input, 2, 29, 3, 5)

        self.hot_fluid_input = QLineEdit("")
        self.hot_fluid_input.setPlaceholderText("hot-fluid")
        self.hot_fluid_input.setFixedSize(280, 70)
        self.MainLayout.addWidget(self.hot_fluid_input, 2, 20, 3, 5)

        self.cold_fluid_input = QLineEdit("")
        self.cold_fluid_input.setPlaceholderText("cold-fluid")
        self.cold_fluid_input.setFixedSize(280, 70)
        self.MainLayout.addWidget(self.cold_fluid_input, 2, 15, 3, 5)

        self.k_solid = QLineEdit("")
        self.k_solid.setPlaceholderText("k-solid")
        self.k_solid.setFixedSize(280, 70)
        self.MainLayout.addWidget(self.k_solid, 2, 10, 3, 5)

        self.htc_input = QLineEdit("")
        self.htc_input.setPlaceholderText("htc")
        self.htc_input.setFixedSize(280, 70)
        self.MainLayout.addWidget(self.htc_input, 2, 5, 3, 5)

        self.tamb_input = QLineEdit("")
        self.tamb_input.setPlaceholderText("Tamb")
        self.tamb_input.setFixedSize(280, 70)
        self.MainLayout.addWidget(self.tamb_input, 3, 5, 3, 5)

        self.nx_input = QLineEdit("")
        self.nx_input.setPlaceholderText("nx")
        self.nx_input.setFixedSize(280, 70)
        self.MainLayout.addWidget(self.nx_input, 3, 10, 3, 5)

        self.z_ch = QLineEdit("")
        self.z_ch.setPlaceholderText("z-ch")
        self.z_ch.setFixedSize(280, 70)
        self.MainLayout.addWidget(self.z_ch, 3, 15, 3, 5)

        self.y_ch = QLineEdit("")
        self.y_ch.setPlaceholderText("y-ch")
        self.y_ch.setFixedSize(280, 70)
        self.MainLayout.addWidget(self.y_ch, 3, 20, 3, 5)

        self.ny = QLineEdit("")
        self.ny.setPlaceholderText("ny")
        self.ny.setFixedSize(280, 70)
        self.MainLayout.addWidget(self.ny, 3, 29, 3, 5)

        self.solid_denstiny = QLineEdit("")
        self.solid_denstiny.setPlaceholderText("solid-destiny")
        self.ny.setFixedSize(280, 70)
        self.MainLayout.addWidget(self.ny, 3, 29, 3, 5)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LogoWindow()
    window.show()
    sys.exit(app.exec_())
