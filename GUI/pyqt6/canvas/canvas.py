import sys

from PySide6.QtWidgets import (QWidget, QLabel, QMainWindow, QApplication,
                               QGraphicsScene, QGraphicsView, QGraphicsTextItem, QGraphicsLineItem,
                               QGraphicsEllipseItem, QGraphicsItem, QGraphicsItemGroup)
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QPixmap, QPainter, QColor, QBrush, QPen, QTransform
import canvas_ui as canvas_ui


class Canvas(QGraphicsScene):

    def __init__(self, w, h):
        super().__init__()
        self.label = QLabel()
        self.setSceneRect(0, 0, w, h)
        self.pos_x = 0
        self.pos_y = 0
        self.current_node_num = 0
        self.node_num_list = list()
        self.node_item_list = list()
        self.node_label_list = list()
        self.node_pos_list = list()
        self.link_node_list = list()
        self.link_list = list()
        self.link_pos_list = list()  # x1,y1,x2,y2

        self.current_clicked_item: QGraphicsItem = None
        self.pre_clicked_item: QGraphicsItem = None

    def set_scene_size(self, w, h):
        self.setSceneRect(0, 0, w, h)

    def clear_canvas(self):
        self.clear()
        print('clear canvas')

    def reset_canvas(self):
        self.current_node_num = 0
        self.clear_canvas()
        self.node_pos_list.clear()
        self.node_item_list.clear()
        self.node_label_list.clear()
        self.link_list.clear()
        self.link_pos_list.clear()
        self.pre_clicked_item = None
        self.current_clicked_item = None

    def draw_marker(self, pos_x, pos_y):
        item = PointItem(self.current_node_num)
        self.addItem(item)
        item.setPos(0, 0)
        item.moveBy(pos_x, pos_y)
        print('draw a marker')
        self.node_item_list.append(item.ellipse_item)
        self.node_label_list.append(item.text_item)

        self.current_node_num += 1

    def draw_line(self, x1, y1, x2, y2):
        print('drawing line')
        line = QGraphicsLineItem(x1, y1, x2, y2)
        self.addItem(line)
        self.link_pos_list.append([x1, y1, x2, y2])
        self.link_list.append(line)

    def mousePressEvent(self, event):
        self.current_mouse_x = event.scenePos().x()
        self.current_mouse_y = event.scenePos().y()
        print(
            f'mouse pressed - x:{self.current_mouse_x}, y:{self.current_mouse_y}')

        if event.button() == Qt.LeftButton:
            self.draw_marker(self.current_mouse_x, self.current_mouse_y)
            self.node_num_list.append(self.current_node_num)
            self.node_pos_list.append(
                [self.current_mouse_x, self.current_mouse_y])

        elif event.button() == Qt.LeftButton:
            self.current_clicked_item = self.itemAt(
                self.current_mouse_x, self.current_mouse_y, QTransform())
            print(
                f'point at x:{self.current_mouse_x}, y:{self.current_mouse_y}, item is {self.current_clicked_item}')

        elif event.button() == Qt.RightButton:
            self.current_clicked_item = self.itemAt(
                self.current_mouse_x, self.current_mouse_y, QTransform())
            print(f'right click, clicked item : {self.current_clicked_item}')

            if self.current_clicked_item != None:

                if self.current_clicked_item in self.node_item_list:
                    item_idx = self.node_item_list.index(
                        self.current_clicked_item)
                    self.remove_item(item_idx)

                if self.current_clicked_item in self.node_label_list:
                    item_idx = self.node_label_list.index(
                        self.current_clicked_item)
                    self.remove_item(item_idx)

        # elif event.button() == Qt.LeftButton and self.opt == "Link":
        #     self.current_clicked_item = self.itemAt(
        #         self.current_mouse_x, self.current_mouse_y, QTransform())
        #     print(f'right click, clicked item : {self.current_clicked_item}')

        #     if self.current_clicked_item != None and self.current_clicked_item.__class__.__name__ == 'QGraphicsEllipseItem':

        #         if self.pre_clicked_item != None:
        #             pre_item_idx = self.node_item_list.index(
        #                 self.pre_clicked_item)
        #             item_idx = self.node_item_list.index(
        #                 self.current_clicked_item)

        #             pre_item_pos = self.node_pos_list[pre_item_idx]
        #             current_item_pos = self.node_pos_list[item_idx]

        #             self.draw_line(x1=pre_item_pos[0],
        #                            y1=pre_item_pos[1],
        #                            x2=current_item_pos[0],
        #                            y2=current_item_pos[1])

        #             self.link_node_list.append(
        #                 [self.node_num_list[pre_item_idx], self.node_num_list[item_idx]])
        #             self.link_pos_list.append(
        #                 [self.node_pos_list[pre_item_idx], self.node_pos_list[item_idx]])

        #             self.pre_clicked_item = self.current_clicked_item

        #         else:
        #             self.pre_clicked_item = self.current_clicked_item

    # def mouseReleaseEvent(self, event):
        # x = event.scenePos().x()
        # y = event.scenePos().y()
        # print(f'mouse released - x:{x}, y:{y}')

        # if event.button() == Qt.LeftButton:
        #     self.current_clicked_item = None
        #     self.pre_clicked_item = None

    # def mouseMoveEvent(self, event):
    #     x = event.scenePos().x()
    #     y = event.scenePos().y()
    #     dx = x - self.current_mouse_x
    #     dy = y - self.current_mouse_y
    #     if self.opt == "Select":
    #         if self.current_clicked_item != None:
    #             if self.current_clicked_item in self.node_item_list:
    #                 item_idx = self.node_item_list.index(
    #                     self.current_clicked_item)
    #                 self.move_node(item_idx, dx, dy)

    #             elif self.current_clicked_item in self.node_label_list:
    #                 item_idx = self.node_label_list.index(
    #                     self.current_clicked_item)
    #                 self.move_node(item_idx, dx, dy)

    #     self.current_mouse_x = x
    #     self.current_mouse_y = y

    def move_node(self, item_idx, dx, dy):
        node_item = self.node_item_list[item_idx]
        node_item.moveBy(dx, dy)
        node_label_item = self.node_label_list[item_idx]
        node_label_item.moveBy(dx, dy)

    def remove_item(self, item_idx):
        node_item = self.node_item_list[item_idx]
        node_label_item = self.node_label_list[item_idx]
        self.removeItem(node_item)
        self.removeItem(node_label_item)
        self.node_num_list.pop(item_idx)
        self.node_item_list.pop(item_idx)
        self.node_label_list.pop(item_idx)
        self.node_pos_list.pop(item_idx)


class PointItem(QGraphicsItemGroup):

    draw_text_flag = True

    ellipse_x = -5
    ellipse_y = -5
    ellipse_width = 11
    ellipse_height = 11

    text_x = 0
    text_y = 0

    def __init__(self, node_num):
        super().__init__()
        self.setFlags(
            QGraphicsItem.GraphicsItemFlag.ItemIsMovable |
            QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)

        self.ellipse_item = QGraphicsEllipseItem(
            self.ellipse_x,
            self.ellipse_y,
            self.ellipse_width,
            self.ellipse_height)

        self.text = f'N_{node_num}'
        self.text_item = QGraphicsTextItem(self.text)

        self.addToGroup(self.ellipse_item)
        self.addToGroup(self.text_item)
