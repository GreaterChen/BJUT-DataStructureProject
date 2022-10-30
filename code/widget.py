# -*- coding: utf-8 -*-
import copy
import threading
from TSP_GA import *
from TSP_BackTrack import *
from DrawImage import *
from School_Intro import *
from Settings import *
from ByOrder import *
from SaveConfirm import *
from Bubble import *


# noinspection PyAttributeOutsideInit
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.selected_pos = []
        self.Main_text = ''
        self.road = Route()
        self.BubbleOpacity = 0.50

        self.del_pos = None

        self.tsp_backtrack = TSP_BackTrack()
        self.IsNBG = False
        self.AddofFigure = "D:\\Grade_3.1\\DS\\project\\result"
        self.Roll = Intro_UI()
        self.Settings = Ui_Settings()
        self.setupUi(self)
        self.getConfig()
        self.setShadow()

    def setupUi(self, Widget):
        # 主体界面
        Widget.setObjectName("Widget")
        Widget.resize(1920, 1080)
        Widget.setMinimumSize(QSize(1920, 1080))
        Widget.setMaximumSize(QSize(1920, 1080))

        # 大地图
        self.schoolmap = QLabel(Widget)
        self.schoolmap.setGeometry(QRect(0, 135, 1468, 945))  # (0,135,1468,945)
        self.schoolmap.setText("")
        self.schoolmap.setPixmap(QPixmap("../images/school_map.jpg"))
        self.schoolmap.setScaledContents(True)
        self.schoolmap.setObjectName("schoolmap")

        # 标题
        self.biaoti = QLabel(Widget)
        self.biaoti.setGeometry(QRect(160, 0, 1300, 135))
        font_biaoti = QFont()
        font_biaoti.setFamily("陈静的字完整版")
        font_biaoti.setPointSize(48)
        self.biaoti.setFont(font_biaoti)
        self.biaoti.setObjectName("biaoti")

        self.MainText = QTextBrowser(Widget)
        self.MainText.setGeometry(QRect(1480, 260, 400, 725))
        self.MainText.setMinimumSize(QSize(400, 725))
        self.MainText.setMaximumSize(QSize(400, 725))
        self.MainText.setObjectName("MainText")
        self.MainText.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        font_MainText = QFont()
        font_MainText.setPointSize(12)
        self.MainText.setFont(font_MainText)
        self.MainText.setText(
            "<p>也正是因为这种特性，微软仅建议将 Mica 用在窗口的基础图层上。如此一来既能起到突出窗口主体的效果，又不会因为应用在弹窗这种地方但却无法实时透明带来令人困惑的视觉效果。事实上，如果仅仅从视觉效果上来说，Mica 更像是一种亚克力的「低配版」，或者说 Windows 11 针对一些需要长时间、频繁打开的窗口（比如资源管理器、系统设置）推出的「低功耗定制版」。如果运用得当，它比传统的纯色窗口标题栏更加温婉、细腻，同时又不会像亚克力那样带来太多额外的性能开销。其他方面 Mica 则与亚克力大同小异了，比如支持明、暗色切换，在窗口失焦时会自动回落到纯色效果等等。<p>")
        self.MainText.textChanged.connect(self.Savelog)

        self.xiaohui = QLabel(Widget)
        self.xiaohui.setGeometry(QRect(200, 10, 111, 111))
        # self.xiaohui.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.xiaohui.setText("")
        self.xiaohui.setPixmap(QPixmap("../images/xiaohui_2.png"))
        self.xiaohui.setScaledContents(True)
        self.xiaohui.setObjectName("xiaohui")

        self.tubiao_1 = QLabel(Widget)
        self.tubiao_1.setGeometry(QRect(1280, 10, 111, 111))
        self.tubiao_1.setText("")
        self.tubiao_1.setPixmap(QPixmap("../images/t1.png"))
        self.tubiao_1.setScaledContents(True)
        self.tubiao_1.setObjectName("tubiao_1")

        self.layoutWidget = QWidget(Widget)
        self.layoutWidget.setGeometry(QRect(1480, 10, 405, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # 实时显示时间
        self.Timer = QLabel(self.layoutWidget)
        self.Timer.setObjectName("Timer")
        font_timer = QFont()
        font_timer.setPointSize(18)
        self.Timer.setFont(font_timer)

        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.showTime)
        self.verticalLayout.addWidget(self.Timer)

        # 第一行按钮
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.view_model = QPushButton(self.layoutWidget)
        self.view_model.setMinimumSize(QSize(95, 50))
        self.view_model.setMaximumSize(QSize(95, 50))
        self.view_model.setObjectName("view_model")
        self.view_model.clicked.connect(self.ViewModel)
        self.horizontalLayout_3.addWidget(self.view_model)

        self.guide_model = QPushButton(self.layoutWidget)
        self.guide_model.setMinimumSize(QSize(95, 50))
        self.guide_model.setMaximumSize(QSize(95, 50))
        self.guide_model.setObjectName("guide_model")
        self.guide_model.setEnabled(False)
        self.guide_model.clicked.connect(self.GuideModel)
        self.horizontalLayout_3.addWidget(self.guide_model)

        self.school_intro = QPushButton(self.layoutWidget)
        self.school_intro.setMinimumSize(QSize(95, 50))
        self.school_intro.setMaximumSize(QSize(95, 50))
        self.school_intro.setObjectName("school_intro")
        self.school_intro.clicked.connect(self.Intro)
        self.horizontalLayout_3.addWidget(self.school_intro)

        self.how_to_use = QPushButton(self.layoutWidget)
        self.how_to_use.setMinimumSize(QSize(95, 50))
        self.how_to_use.setMaximumSize(QSize(95, 50))
        self.how_to_use.setObjectName("how_to_use")
        self.horizontalLayout_3.addWidget(self.how_to_use)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        # 第二行按钮

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.settings = QPushButton(self.layoutWidget)
        self.settings.setMinimumSize(QSize(95, 50))
        self.settings.setMaximumSize(QSize(95, 50))
        self.settings.setObjectName("settings")
        self.settings.clicked.connect(self.SetSettings)

        self.horizontalLayout.addWidget(self.settings)

        self.GetBack = QPushButton(self.layoutWidget)
        self.GetBack.setMinimumSize(QSize(95, 50))
        self.GetBack.setMaximumSize(QSize(95, 50))
        self.GetBack.setObjectName("GetBack")
        self.GetBack.clicked.connect(self.GetBackStep)
        self.horizontalLayout.addWidget(self.GetBack)

        self.ChangeRoad = QPushButton(self)
        self.ChangeRoad.setGeometry(QRect(100, 170, 95, 50))
        self.ChangeRoad.setStyleSheet("background:rgb(197, 225, 184)")
        self.ChangeRoad.setObjectName("ChangeRoad")

        self.GetBetterRoad = QPushButton(self)
        self.GetBetterRoad.setGeometry(QRect(100, 240, 95, 50))
        self.GetBetterRoad.setStyleSheet("background:rgb(197, 225, 184)")
        self.GetBetterRoad.setObjectName("GetBetterRoad")
        self.GetBetterRoad.clicked.connect(self.BetterRoad)

        self.Start = QPushButton(self)
        self.Start.setGeometry(QRect(100, 310, 95, 50))
        self.Start.setStyleSheet("background:rgb(197, 225, 184)")
        self.Start.setObjectName("Start")
        self.Start.clicked.connect(self.Go)

        # 清除全部选择
        self.clearall = QPushButton(self.layoutWidget)
        self.clearall.setMinimumSize(QSize(95, 50))
        self.clearall.setMaximumSize(QSize(95, 50))
        self.clearall.setObjectName("clearall")
        self.clearall.clicked.connect(self.ClearAll)
        self.horizontalLayout.addWidget(self.clearall)

        self.GetRoad = QPushButton(self.layoutWidget)
        self.GetRoad.setMinimumSize(QSize(95, 50))
        self.GetRoad.setMaximumSize(QSize(95, 50))
        self.GetRoad.setObjectName("GetRoad")
        self.GetRoad.clicked.connect(self.get_TSP)
        self.horizontalLayout.addWidget(self.GetRoad)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.groupBox = QGroupBox(self.layoutWidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setMouseTracking(False)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget1 = QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QRect(30, 30, 361, 21))
        self.layoutWidget1.setObjectName("layoutWidget1")

        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.TSP_button = QRadioButton(self.layoutWidget1)
        self.TSP_button.setObjectName("TSP_button")
        self.horizontalLayout_2.addWidget(self.TSP_button)

        self.TSPwr_button = QRadioButton(self.layoutWidget1)
        self.TSPwr_button.setObjectName("TSPwr_button")
        self.horizontalLayout_2.addWidget(self.TSPwr_button)

        self.by_order_button = QRadioButton(self.layoutWidget1)
        self.by_order_button.setObjectName("by_order_button")

        self.horizontalLayout_2.addWidget(self.by_order_button)
        self.verticalLayout.addWidget(self.groupBox)
        self.init_button()

        self.retranslateUi(Widget)
        QMetaObject.connectSlotsByName(Widget)

    def init_button(self):
        # 地点定位
        self.A1 = QPushButton(self)
        self.A1.setGeometry(QRect(550, 280, 101, 21))
        self.A1.setObjectName("A1")
        self.A2 = QPushButton(self)
        self.A2.setGeometry(QRect(680, 240, 71, 71))
        self.A2.setObjectName("A2")
        self.A0 = QPushButton(self)
        self.A0.setGeometry(QRect(550, 250, 101, 21))
        self.A0.setObjectName("A0")
        self.A3 = QPushButton(self)
        self.A3.setGeometry(QRect(750, 240, 93, 31))
        self.A3.setObjectName("A3")
        self.A4 = QPushButton(self)
        self.A4.setGeometry(QRect(750, 280, 93, 31))
        self.A4.setObjectName("A4")
        self.A5 = QPushButton(self)
        self.A5.setGeometry(QRect(840, 250, 61, 28))
        self.A5.setObjectName("A5")
        self.A6 = QPushButton(self)
        self.A6.setGeometry(QRect(840, 280, 61, 41))
        self.A6.setObjectName("A6")
        self.A7 = QPushButton(self)
        self.A7.setGeometry(QRect(900, 290, 71, 28))
        self.A7.setObjectName("A7")
        self.A9 = QPushButton(self)
        self.A9.setGeometry(QRect(540, 330, 111, 51))
        self.A9.setObjectName("A9")
        self.A8 = QPushButton(self)
        self.A8.setGeometry(QRect(450, 390, 51, 61))
        self.A8.setObjectName("A8")
        self.A10 = QPushButton(self)
        self.A10.setGeometry(QRect(540, 380, 41, 91))
        self.A10.setObjectName("A10")
        self.A11 = QPushButton(self)
        self.A11.setGeometry(QRect(540, 460, 121, 61))
        self.A11.setObjectName("A11")
        self.A12 = QPushButton(self)
        self.A12.setGeometry(QRect(700, 357, 111, 31))
        self.A12.setObjectName("A12")
        self.A13 = QPushButton(self)
        self.A13.setGeometry(QRect(750, 390, 81, 51))
        self.A13.setObjectName("A13")
        self.A14 = QPushButton(self)
        self.A14.setGeometry(QRect(680, 460, 121, 61))
        self.A14.setObjectName("A14")
        self.A15 = QPushButton(self)
        self.A15.setGeometry(QRect(810, 450, 61, 41))
        self.A15.setObjectName("A15")
        self.A16 = QPushButton(self)
        self.A16.setGeometry(QRect(840, 330, 151, 28))
        self.A16.setObjectName("A16")
        self.A17 = QPushButton(self)
        self.A17.setGeometry(QRect(890, 360, 93, 151))
        self.A17.setObjectName("A17")
        self.A18 = QPushButton(self)
        self.A18.setGeometry(QRect(1010, 400, 93, 61))
        self.A18.setObjectName("A18")
        self.A19 = QPushButton(self)
        self.A19.setGeometry(QRect(1010, 330, 61, 51))
        self.A19.setObjectName("A19")
        self.A20 = QPushButton(self)
        self.A20.setGeometry(QRect(1010, 480, 101, 41))
        self.A20.setObjectName("A20")
        self.A21 = QPushButton(self)
        self.A21.setGeometry(QRect(540, 620, 71, 81))
        self.A21.setObjectName("A21")
        self.A22 = QPushButton(self)
        self.A22.setGeometry(QRect(630, 610, 71, 81))
        self.A22.setObjectName("A22")
        self.A23 = QPushButton(self)
        self.A23.setGeometry(QRect(730, 570, 151, 51))
        self.A23.setObjectName("A23")
        self.A24 = QPushButton(self)
        self.A24.setGeometry(QRect(730, 620, 71, 51))
        self.A24.setAcceptDrops(False)
        self.A24.setObjectName("A24")
        self.A25 = QPushButton(self)
        self.A25.setGeometry(QRect(730, 670, 71, 41))
        self.A25.setObjectName("A25")
        self.A26 = QPushButton(self)
        self.A26.setGeometry(QRect(730, 710, 71, 41))
        self.A26.setObjectName("A26")
        self.A27 = QPushButton(self)
        self.A27.setGeometry(QRect(800, 620, 81, 28))
        self.A27.setObjectName("A27")
        self.A28 = QPushButton(self)
        self.A28.setGeometry(QRect(800, 650, 81, 28))
        self.A28.setObjectName("A28")
        self.A29 = QPushButton(self)
        self.A29.setGeometry(QRect(800, 690, 93, 28))
        self.A29.setObjectName("A29")
        self.A30 = QPushButton(self)
        self.A30.setGeometry(QRect(810, 720, 71, 28))
        self.A30.setObjectName("A30")
        self.A31 = QPushButton(self)
        self.A31.setGeometry(QRect(910, 580, 131, 151))
        self.A31.setObjectName("A31")
        self.A32 = QPushButton(self)
        self.A32.setGeometry(QRect(1050, 550, 111, 61))
        self.A32.setObjectName("A32")
        self.A33 = QPushButton(self)
        self.A33.setGeometry(QRect(1190, 547, 81, 141))
        self.A33.setObjectName("A33")
        self.A34 = QPushButton(self)
        self.A34.setGeometry(QRect(1072, 620, 101, 61))
        self.A34.setObjectName("A34")
        self.A35 = QPushButton(self)
        self.A35.setGeometry(QRect(490, 770, 93, 61))
        self.A35.setObjectName("A35")
        self.A36 = QPushButton(self)
        self.A36.setGeometry(QRect(620, 780, 93, 101))
        self.A36.setObjectName("A36")
        self.A37 = QPushButton(self)
        self.A37.setGeometry(QRect(760, 780, 91, 28))
        self.A37.setObjectName("A37")
        self.A38 = QPushButton(self)
        self.A38.setGeometry(QRect(760, 810, 93, 28))
        self.A38.setObjectName("A38")
        self.A39 = QPushButton(self)
        self.A39.setGeometry(QRect(770, 890, 111, 71))
        self.A39.setObjectName("A39")
        self.A40 = QPushButton(self)
        self.A40.setGeometry(QRect(620, 960, 93, 61))
        self.A40.setObjectName("A40")
        self.A41 = QPushButton(self)
        self.A41.setGeometry(QRect(930, 810, 221, 131))
        self.A41.setObjectName("A41")
        self.A42 = QPushButton(self)
        self.A42.setGeometry(QRect(1140, 720, 81, 61))
        self.A42.setObjectName("A42")
        self.A43 = QPushButton(self)
        self.A43.setGeometry(QRect(1172, 830, 101, 31))
        self.A43.setObjectName("A43")
        self.A44 = QPushButton(self)
        self.A44.setGeometry(QRect(1220, 800, 93, 31))
        self.A44.setObjectName("A44")
        self.A45 = QPushButton(self)
        self.A45.setGeometry(QRect(1250, 750, 81, 28))
        self.A45.setObjectName("A45")
        self.A46 = QPushButton(self)
        self.A46.setGeometry(QRect(790, 180, 93, 61))
        self.A46.setObjectName("A46")

        self.A0.setFlat(True)
        self.A1.setFlat(True)
        self.A2.setFlat(True)
        self.A3.setFlat(True)
        self.A4.setFlat(True)
        self.A5.setFlat(True)
        self.A6.setFlat(True)
        self.A7.setFlat(True)
        self.A8.setFlat(True)
        self.A9.setFlat(True)
        self.A10.setFlat(True)
        self.A11.setFlat(True)
        self.A12.setFlat(True)
        self.A13.setFlat(True)
        self.A14.setFlat(True)
        self.A15.setFlat(True)
        self.A16.setFlat(True)
        self.A17.setFlat(True)
        self.A18.setFlat(True)
        self.A19.setFlat(True)
        self.A20.setFlat(True)
        self.A21.setFlat(True)
        self.A22.setFlat(True)
        self.A23.setFlat(True)
        self.A24.setFlat(True)
        self.A25.setFlat(True)
        self.A26.setFlat(True)
        self.A27.setFlat(True)
        self.A28.setFlat(True)
        self.A29.setFlat(True)
        self.A30.setFlat(True)
        self.A31.setFlat(True)
        self.A32.setFlat(True)
        self.A33.setFlat(True)
        self.A34.setFlat(True)
        self.A35.setFlat(True)
        self.A36.setFlat(True)
        self.A37.setFlat(True)
        self.A38.setFlat(True)
        self.A39.setFlat(True)
        self.A40.setFlat(True)
        self.A41.setFlat(True)
        self.A42.setFlat(True)
        self.A43.setFlat(True)
        self.A44.setFlat(True)
        self.A45.setFlat(True)
        self.A46.setFlat(True)

        self.A0.clicked.connect(self.BeSelected)
        self.A1.clicked.connect(self.BeSelected)
        self.A2.clicked.connect(self.BeSelected)
        self.A3.clicked.connect(self.BeSelected)
        self.A4.clicked.connect(self.BeSelected)
        self.A5.clicked.connect(self.BeSelected)
        self.A6.clicked.connect(self.BeSelected)
        self.A7.clicked.connect(self.BeSelected)
        self.A8.clicked.connect(self.BeSelected)
        self.A9.clicked.connect(self.BeSelected)
        self.A10.clicked.connect(self.BeSelected)
        self.A11.clicked.connect(self.BeSelected)
        self.A12.clicked.connect(self.BeSelected)
        self.A13.clicked.connect(self.BeSelected)
        self.A14.clicked.connect(self.BeSelected)
        self.A15.clicked.connect(self.BeSelected)
        self.A16.clicked.connect(self.BeSelected)
        self.A17.clicked.connect(self.BeSelected)
        self.A18.clicked.connect(self.BeSelected)
        self.A19.clicked.connect(self.BeSelected)
        self.A20.clicked.connect(self.BeSelected)
        self.A21.clicked.connect(self.BeSelected)
        self.A22.clicked.connect(self.BeSelected)
        self.A23.clicked.connect(self.BeSelected)
        self.A24.clicked.connect(self.BeSelected)
        self.A25.clicked.connect(self.BeSelected)
        self.A26.clicked.connect(self.BeSelected)
        self.A27.clicked.connect(self.BeSelected)
        self.A28.clicked.connect(self.BeSelected)
        self.A29.clicked.connect(self.BeSelected)
        self.A30.clicked.connect(self.BeSelected)
        self.A31.clicked.connect(self.BeSelected)
        self.A32.clicked.connect(self.BeSelected)
        self.A33.clicked.connect(self.BeSelected)
        self.A34.clicked.connect(self.BeSelected)
        self.A35.clicked.connect(self.BeSelected)
        self.A36.clicked.connect(self.BeSelected)
        self.A37.clicked.connect(self.BeSelected)
        self.A38.clicked.connect(self.BeSelected)
        self.A39.clicked.connect(self.BeSelected)
        self.A40.clicked.connect(self.BeSelected)
        self.A41.clicked.connect(self.BeSelected)
        self.A42.clicked.connect(self.BeSelected)
        self.A43.clicked.connect(self.BeSelected)
        self.A44.clicked.connect(self.BeSelected)
        self.A45.clicked.connect(self.BeSelected)
        self.A46.clicked.connect(self.BeSelected)

    def setShadow(self):
        BlurRadius = 5
        effect_shadow_0 = QGraphicsDropShadowEffect(self)
        effect_shadow_0.setOffset(0, 0)
        effect_shadow_0.setBlurRadius(50)
        effect_shadow_0.setColor(Qt.gray)
        effect_shadow_1 = QGraphicsDropShadowEffect(self)
        effect_shadow_1.setOffset(0, 0)
        effect_shadow_1.setBlurRadius(10)
        effect_shadow_1.setColor(Qt.gray)
        effect_shadow_2 = QGraphicsDropShadowEffect(self)
        effect_shadow_2.setOffset(0, 0)
        effect_shadow_2.setBlurRadius(BlurRadius)
        effect_shadow_2.setColor(Qt.gray)
        effect_shadow_3 = QGraphicsDropShadowEffect(self)
        effect_shadow_3.setOffset(0, 0)
        effect_shadow_3.setBlurRadius(BlurRadius)
        effect_shadow_3.setColor(Qt.gray)
        effect_shadow_4 = QGraphicsDropShadowEffect(self)
        effect_shadow_4.setOffset(0, 0)
        effect_shadow_4.setBlurRadius(BlurRadius)
        effect_shadow_4.setColor(Qt.gray)
        effect_shadow_5 = QGraphicsDropShadowEffect(self)
        effect_shadow_5.setOffset(0, 0)
        effect_shadow_5.setBlurRadius(BlurRadius)
        effect_shadow_5.setColor(Qt.gray)
        effect_shadow_6 = QGraphicsDropShadowEffect(self)
        effect_shadow_6.setOffset(0, 0)
        effect_shadow_6.setBlurRadius(BlurRadius)
        effect_shadow_6.setColor(Qt.gray)
        effect_shadow_7 = QGraphicsDropShadowEffect(self)
        effect_shadow_7.setOffset(0, 0)
        effect_shadow_7.setBlurRadius(BlurRadius)
        effect_shadow_7.setColor(Qt.gray)
        effect_shadow_8 = QGraphicsDropShadowEffect(self)
        effect_shadow_8.setOffset(0, 0)
        effect_shadow_8.setBlurRadius(BlurRadius)
        effect_shadow_8.setColor(Qt.gray)
        effect_shadow_9 = QGraphicsDropShadowEffect(self)
        effect_shadow_9.setOffset(0, 0)
        effect_shadow_9.setBlurRadius(BlurRadius)
        effect_shadow_9.setColor(Qt.gray)
        effect_shadow_10 = QGraphicsDropShadowEffect(self)
        effect_shadow_10.setOffset(0, 0)
        effect_shadow_10.setBlurRadius(BlurRadius)
        effect_shadow_10.setColor(Qt.gray)
        effect_shadow_11 = QGraphicsDropShadowEffect(self)
        effect_shadow_11.setOffset(0, 0)
        effect_shadow_11.setBlurRadius(15)
        effect_shadow_11.setColor(Qt.gray)
        effect_shadow_12 = QGraphicsDropShadowEffect(self)
        effect_shadow_12.setOffset(0, 0)
        effect_shadow_12.setBlurRadius(BlurRadius)
        effect_shadow_12.setColor(Qt.gray)

        self.schoolmap.setGraphicsEffect(effect_shadow_0)
        # self.xiaohui.setGraphicsEffect(effect_shadow_1)
        # self.tubiao_1.setGraphicsEffect(effect_shadow_2)
        self.view_model.setGraphicsEffect(effect_shadow_3)
        self.guide_model.setGraphicsEffect(effect_shadow_4)
        self.school_intro.setGraphicsEffect(effect_shadow_5)
        self.how_to_use.setGraphicsEffect(effect_shadow_6)
        self.settings.setGraphicsEffect(effect_shadow_7)
        self.GetBack.setGraphicsEffect(effect_shadow_8)
        self.clearall.setGraphicsEffect(effect_shadow_9)
        self.GetRoad.setGraphicsEffect(effect_shadow_10)
        self.MainText.setGraphicsEffect(effect_shadow_11)
        # self.TSP_button.setGraphicsEffect(effect_shadow_12)

    def retranslateUi(self, Widget):
        _translate = QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "校园导航系统 by clb"))
        self.biaoti.setText(
            _translate("Widget", "<html><head/><body><p align=\"center\">北京工业大学校园导航系统</p></body></html>"))
        self.Timer.setText(_translate("Widget", "<html><head/><body><p align=\"center\">初始化...</p></body></html>"))
        self.settings.setText(_translate("Widget", "设置"))
        self.GetBack.setText(_translate("Widget", "撤销选择"))
        self.clearall.setText(_translate("Widget", "清空选择"))
        self.GetRoad.setText(_translate("Widget", "生成路径"))
        self.view_model.setText(_translate("Widget", "浏览模式"))
        self.guide_model.setText(_translate("Widget", "导航模式"))
        self.school_intro.setText(_translate("Widget", "校园简介"))
        self.how_to_use.setText(_translate("Widget", "使用说明"))
        self.groupBox.setTitle(_translate("Widget", "模式选择"))
        self.TSP_button.setText(_translate("Widget", "TSP"))
        self.TSPwr_button.setText(_translate("Widget", "TSP without return"))
        self.by_order_button.setText(_translate("Widget", "by order"))

        self.GetBetterRoad.setText(_translate("Widget", "简化路线"))
        self.Start.setText(_translate("Widget", "出发"))
        self.ChangeRoad.setText(_translate("Widget", "换条路线"))

        self.A1.setToolTip(_translate("Widget", "宿舍2号楼"))
        self.A2.setToolTip(_translate("Widget", "天天餐厅&学生综合服务大厅"))
        self.A0.setToolTip(_translate("Widget", "宿舍1号楼"))
        self.A3.setToolTip(_translate("Widget", "宿舍3号楼"))
        self.A4.setToolTip(_translate("Widget", "宿舍4号楼"))
        self.A5.setToolTip(_translate("Widget", "校医院"))
        self.A6.setToolTip(_translate("Widget", "北浴室"))
        self.A7.setToolTip(_translate("Widget", "金工楼"))
        self.A9.setToolTip(_translate("Widget", "第一教学楼"))
        self.A8.setToolTip(_translate("Widget", "西门"))
        self.A10.setToolTip(_translate("Widget", "第二教学楼"))
        self.A11.setToolTip(_translate("Widget", "材料楼"))
        self.A12.setToolTip(_translate("Widget", "旧图书馆"))
        self.A13.setToolTip(_translate("Widget", "礼堂"))
        self.A14.setToolTip(_translate("Widget", "数理楼"))
        self.A15.setToolTip(_translate("Widget", "游泳馆"))
        self.A16.setToolTip(_translate("Widget", "宿舍10&11号楼"))
        self.A17.setToolTip(_translate("Widget", "北操"))
        self.A18.setToolTip(_translate("Widget", "宿舍13&14号楼"))
        self.A19.setToolTip(_translate("Widget", "东门"))
        self.A20.setToolTip(_translate("Widget", "能源楼"))
        self.A21.setToolTip(_translate("Widget", "信息楼"))
        self.A22.setToolTip(_translate("Widget", "逸夫图书馆"))
        self.A23.setToolTip(_translate("Widget", "第三教学楼"))
        self.A24.setToolTip(_translate("Widget", "知心园"))
        self.A25.setToolTip(_translate("Widget", "宿舍9号楼"))
        self.A26.setToolTip(_translate("Widget", "美食园"))
        self.A27.setToolTip(_translate("Widget", "宿舍7号楼"))
        self.A28.setToolTip(_translate("Widget", "宿舍8号楼"))
        self.A29.setToolTip(_translate("Widget", "宿舍12号楼"))
        self.A30.setToolTip(_translate("Widget", "奥运餐厅"))
        self.A31.setToolTip(_translate("Widget", "南操"))
        self.A32.setToolTip(_translate("Widget", "第四教学楼"))
        self.A33.setToolTip(_translate("Widget", "理科楼"))
        self.A34.setToolTip(_translate("Widget", "艺术楼"))
        self.A35.setToolTip(_translate("Widget", "经管楼"))
        self.A36.setToolTip(_translate("Widget", "科学楼"))
        self.A37.setToolTip(_translate("Widget", "宿舍5号楼"))
        self.A38.setToolTip(_translate("Widget", "宿舍6号楼"))
        self.A39.setToolTip(_translate("Widget", "人文楼"))
        self.A40.setToolTip(_translate("Widget", "南门"))
        self.A41.setToolTip(_translate("Widget", "奥运场馆"))
        self.A42.setToolTip(_translate("Widget", "月亮湖"))
        self.A43.setToolTip(_translate("Widget", "知行楼(实训楼)"))
        self.A44.setToolTip(_translate("Widget", "交通楼"))
        self.A45.setToolTip(_translate("Widget", "软件楼"))
        self.A46.setToolTip(_translate("Widget", "北门"))

    def get_TSP(self):
        if self.TSP_button.isChecked():
            if len(self.selected_pos) == 0 or len(self.selected_pos) == 1:
                QMessageBox.warning(self, '警告', '请选择至少两个目的地')
                return
            self.GetRoad.setEnabled(False)
            self.GetBack.setEnabled(False)
            if self.AlgorithmModel == 0:
                if len(self.selected_pos) >= 8:
                    t = TSP_GA(self.selected_pos)
                    self.road = t.run(20)
                else:
                    self.road = copy.deepcopy(self.tsp_backtrack.run(self.selected_pos))
                    self.tsp_backtrack.ClearAll()


            elif self.AlgorithmModel == 1:
                t = TSP_GA(self.selected_pos)
                self.road = t.run(20)

            elif self.AlgorithmModel == 2:
                t = TSP_BackTrack()
                self.road = self.tsp_backtrack.run(self.selected_pos)
                t.ClearAll()

            self.Main_text = f"总距离：{round(self.road.min_distance, 2)} m\n"
            self.Main_text += f"预计用时：{int(self.road.min_distance / 66.6)}分{int((self.road.min_distance / 66.6 - int(self.road.min_distance / 66.6)) * 60)}秒\n"
            self.Main_text += "路径如下：\n"
            for i in self.road.simple_citys_name:
                self.Main_text += '\t'
                self.Main_text += i
                self.Main_text += '->\n'

            self.Main_text += '\t'
            self.Main_text += self.road.simple_citys_name[0]
            self.Main_text += '\n'

            self.Main_text += "详细路径如下：\n"
            for i in self.road.entire_citys_name:
                self.Main_text += '\t'
                self.Main_text += i
                self.Main_text += '->\n'

            self.Main_text += '\t'
            self.Main_text += self.road.entire_citys_name[0]
            self.Main_text += '\n'


            self.MainText.setText(self.Main_text)

            d = DrawRoad(self.AddofFigure)
            d.DrawImage(self.road)
            self.schoolmap.setPixmap(QPixmap("../images/school_map_change.jpg"))
        elif self.TSPwr_button.isChecked():
            pass
        elif self.by_order_button.isChecked():
            order = ByOrder(self.selected_pos)
            self.road = order.GetRoad()
            # self.Main_text = str(self.simple_road) + '\n' + str(self.entire_road)
            self.MainText.setText(self.Main_text)
            d = DrawRoad(self.AddofFigure)
            # d.DrawImage_order(self.entire_road, self.simple_road)
            self.schoolmap.setPixmap(QPixmap("../images/school_map_change.jpg"))
        else:
            QMessageBox.warning(self, '警告', '请选择模式')

        desktop = QApplication.desktop()
        t = TipUi('结果已保存', desktop.width() / 2, desktop.height() / 2)
        t.show()
        self.DrawBubble()

    def showTime(self):
        Time = QDateTime.currentDateTime()  # 系统时间
        timeDisplay = Time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.Timer.setText(timeDisplay)

    def GuideModel(self):
        self.guide_model.setEnabled(False)
        self.view_model.setEnabled(True)

    def ViewModel(self):
        self.guide_model.setEnabled(True)
        self.view_model.setEnabled(False)

    def ClearAll(self):
        if self.GetRoad.isEnabled() == False:
            for item in self.selected_pos:
                exec("self.B{}.close()".format(item))

        self.selected_pos.clear()
        self.road = Route()
        self.Main_text = ''
        self.MainText.setText('已清空所有选择')

        self.GetRoad.setEnabled(True)
        self.schoolmap.setPixmap(QPixmap("../images/school_map.jpg"))

    def BeSelected(self):
        btn = self.sender()
        name = btn.objectName()
        real_name = btn.toolTip()
        num = int(name[1:])
        if num in self.selected_pos:
            self.selected_pos.remove(num)
            string = '已删除:' + real_name
            self.Main_text += string + '\n'
            self.MainText.setText(self.Main_text)
        else:
            self.selected_pos.append(num)
            string = '已选中:' + real_name
            self.Main_text += string + '\n'
            self.MainText.setText(self.Main_text)

    def Intro(self):
        self.Roll.showMaximized()
        self.Roll.show()

    def SetSettings(self):
        self.Settings.setWindowModality(Qt.ApplicationModal)  # 子窗口堵塞父窗口
        self.Settings.show()
        self.Settings.Signal_background.connect(self.ChangeBG)
        self.Settings.Signal_textBrowser.connect(self.ChangeTB)
        self.Settings.Signal_model.connect(self.ChangeModel)
        self.Settings.Signal_Algorithm.connect(self.ChangeAlgorithm)
        self.Settings.Signal_AddofFigure.connect(self.ChangeAdd)
        self.Settings.Signal_Opacity.connect(self.ChangeOpacity)

    def ChangeBG(self, model):
        if model == 0:
            palette = QPalette()
            self.setPalette(palette)
            self.IsNBG = True
        elif model == 1:
            palette = QPalette()
            palette.setBrush(QPalette.Background, QBrush(QPixmap("../images/background_1.jpg")))
            self.setPalette(palette)
        elif model == 2:
            palette = QPalette()
            palette.setBrush(QPalette.Background, QBrush(QPixmap("../images/background_2.jpg")))
            self.setPalette(palette)

    def ChangeTB(self, model):
        if model == 0:
            effect_shadow = QGraphicsDropShadowEffect(self)
            effect_shadow.setOffset(0, 0)
            self.MainText.setGraphicsEffect(effect_shadow)
            self.MainText.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        else:
            effect_shadow = QGraphicsDropShadowEffect(self)
            effect_shadow.setOffset(0, 0)
            effect_shadow.setBlurRadius(20)
            effect_shadow.setColor(Qt.gray)
            self.MainText.setGraphicsEffect(effect_shadow)
            self.MainText.setStyleSheet("background:")

    def ChangeModel(self, model):
        if model == 0:
            self.TSP_button.setChecked(True)
        elif model == 1:
            self.TSPwr_button.setChecked(True)
        elif model == 2:
            self.by_order_button.setChecked(True)

    def ChangeAlgorithm(self, model):
        if model == 0:
            self.AlgorithmModel = 0
        elif model == 1:
            self.AlgorithmModel = 1
        elif model == 2:
            self.AlgorithmModel = 2

    def ChangeAdd(self, add):
        self.AddofFigure = add

    def ChangeOpacity(self, value):
        self.BubbleOpacity = value / 100

    def getConfig(self):
        with open("config.txt") as f:
            text = f.read().split(' ')

        if text[0] == '0':
            palette = QPalette()
            self.setPalette(palette)
            self.IsNBG = False
        elif text[0] == '1':
            palette = QPalette()
            palette.setBrush(QPalette.Background, QBrush(QPixmap("../images/background_1.jpg")))
            self.setPalette(palette)
        elif text[0] == '2':
            palette = QPalette()
            palette.setBrush(QPalette.Background, QBrush(QPixmap("../images/background_2.jpg")))
            self.setPalette(palette)

        if text[1] == '0':
            self.TSP_button.setChecked(True)
        elif text[1] == '1':
            self.TSPwr_button.setChecked(True)
        elif text[1] == '2':
            self.by_order_button.setChecked(True)

        if text[2] == '0':
            self.AlgorithmModel = 0
        elif text[2] == '1':
            self.AlgorithmModel = 1
        elif text[2] == '2':
            self.AlgorithmModel = 2

        if text[3] == '0':
            effect_shadow = QGraphicsDropShadowEffect(self)
            effect_shadow.setOffset(0, 0)
            self.MainText.setGraphicsEffect(effect_shadow)
            self.MainText.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        else:
            if self.IsNBG:
                effect_shadow = QGraphicsDropShadowEffect(self)
                effect_shadow.setOffset(0, 0)
                effect_shadow.setBlurRadius(20)
                effect_shadow.setColor(Qt.gray)
                self.MainText.setGraphicsEffect(effect_shadow)
                self.MainText.setStyleSheet("background:")
            else:
                self.MainText.setStyleSheet("background:")

        self.AddofFigure = text[4]

        self.BubbleOpacity = int(text[5]) / 100

    def GetBackStep(self):
        self.Main_text += "已删除："
        exec(f"text = self.A{self.selected_pos[-1]}.toolTip()\n")
        exec("self.Main_text += text")
        self.MainText.setText(self.Main_text)
        self.selected_pos.pop()

    def DrawBubble(self):
        self.Bubble_pos = []
        for i, item in enumerate(self.road.simple_road[0:-1]):
            # exec(f"name = self.road.")
            exec(f"self.B{item} = UI_Bubble(item,self.BubbleOpacity,self.road.simple_citys_name[i],self.road.signle_distance[i])")
            exec(f"self.B{item}.setWindowOpacity(self.BubbleOpacity)")
            exec(f"self.B{item}.show()")
            exec(f"self.Bubble_pos.append([self.B{item}.pos().x(),self.B{item}.pos().y()])")

        exec("self.B{}.exec_()".format(self.selected_pos[0]))

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        if self.GetRoad.isEnabled() == False:
            for item in self.selected_pos:
                exec("self.B{}.close()".format(item))

    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            if self.windowState() & Qt.WindowMinimized:
                if self.GetRoad.isEnabled() == False:
                    for item in self.selected_pos:
                        exec("self.B{}.setVisible(False)".format(item))
                    return

            if Qt.WindowMaximized:
                if self.GetRoad.isEnabled() == False:
                    for item in self.selected_pos:
                        exec("self.B{}.setVisible(True)".format(item))
                    return

    def moveEvent(self, QMoveEvent):
        if self.GetRoad.isEnabled() == False:
            for i, item in enumerate(self.selected_pos):
                exec(
                    f"self.B{item}.move(self.Bubble_pos[{i}][0] + self.pos().x(),self.Bubble_pos[{i}][1] + self.pos().y())")

    def BetterRoad(self):
        if self.GetRoad.isEnabled():
            QMessageBox.warning(self, "警告", "请先生成路径")
            return
        if len(self.selected_pos) <= 2:
            QMessageBox.information(self, "提示", "路径已经很短啦")
            return

        self.new_road = Route()
        threading_list = []
        for item in self.selected_pos:
            t = threading.Thread(target=self.CalculateBetter, args=(item,))
            t.start()
            threading_list.append(t)
        for t in threading_list:
            t.join()
        self.new_road.GetCitysName()

        self.Main_text += "\n已为您智能略去目的地："
        exec(f"text = self.A{self.del_pos}.toolTip()")
        exec("self.Main_text += text ")
        self.Main_text += '\n减少的的距离为：'
        decrease_dis = str(round(self.road.min_distance - self.new_road.min_distance, 2))
        self.Main_text += f"{decrease_dis} m\n"
        self.Main_text += f"当前总距离：{round(self.new_road.min_distance, 2)} m\n"
        self.Main_text += "预计用时:{}分{}秒\n".format(int(self.new_road.min_distance / 66.6),
                                                 int((self.new_road.min_distance / 66.6 - int(self.new_road.min_distance / 66.6)) * 60))

        self.MainText.setText(self.Main_text)

        d = DrawRoad(self.AddofFigure)
        d.DrawImage(self.new_road)
        self.schoolmap.setPixmap(QPixmap("../images/school_map_change.jpg"))
        exec(f"self.B{self.del_pos}.close()")
        self.selected_pos.remove(self.del_pos)
        for item in self.selected_pos:
            exec(f"self.B{item}.GoGoGo()")

    def CalculateBetter(self, item):
        pos = self.selected_pos.copy()
        pos.remove(item)
        road = copy.deepcopy(self.tsp_backtrack.run(pos))
        if road.min_distance < self.new_road.min_distance:
            self.new_road.min_distance = road.min_distance
            self.new_road.simple_road = road.simple_road
            self.new_road.entire_road = road.entire_road
            self.del_pos = item
        self.tsp_backtrack.ClearAll()

    def Go(self):
        for item in self.selected_pos:
            exec(f"self.B{item}.GoGoGo()")

    def Savelog(self):
        add = self.AddofFigure + '/res.txt'
        with open(add,"w") as f:
            f.write(self.MainText.toPlainText())

