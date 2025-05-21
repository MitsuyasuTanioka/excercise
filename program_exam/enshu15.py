class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.back = None
        self.check = False

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return
        else:
            current = self.root  # 現在のノード
            # back_current = self.root  # 現在のノードの1つ前のノード(初期値ルート)
            while True:
                if value <= current.value:  # 現在のノードの値以下だった時
                    if current.left is None:  # さらに左のノード(値が小さいほうのノード)がないとき
                        current.left = newNode  # 現在のノードの左のノードとして設定
                        current.left.back = current  # 現在の左のノードの1つ前のノードとして現在のノードを設定
                        return
                    else:
                        # back_current = current
                        current = current.left
                else:
                    if current.right is None:
                        current.right = newNode
                        current.right.back = current
                        return
                    else:
                        # back_current = current
                        current = current.right

    def printlist(self):
        #resultに順番に数値を入れていく
        result = []
        #cuurenは現在の場所を示す
        current = self.root
        # 全部リストに入れたらFalseになる
        flag = True

        while flag:
            while current.left is not None: #現在のノードからいけるとこまで左に進む
                current = current.left
            result.append(current.value) #先ほどのノードの一番左まで降りてきたら、その値をリストに入れる
            current.check = True # 追加したノードに関してはチェックする
            while current.right is None or current.right.check == True: # 現在のノードの右側がない状態か、現在のノードの右側が追加済みの間、実行
                if current.right is None: # 右側にノードがない状態の時
                    current = current.back  # 1つ前に戻る
                    if current.check == False:
                        result.append(current.value)  # 1つ前に戻ったのちにそのノードの値を追加する
                        current.check = True  # リストに追加したので追加済みにする
                else: # 右側にノードはあるが、そのノードが既にリストに追加済みの時
                    if current.back is None:  # さらに現在のノードがルートであるとき
                        flag = False  # すべての値の追加が完了したのでflagをFalseに
                        break
                    current = current.back  # 1つ前のノードに戻る
                    if current.check is False:
                        result.append(current.value)  # 1つ前に戻ったのちにそのノードの値を追加する
                        current.check = True  # リストに追加したので追加済みにする
                # if current.check is True: # 現在のノードがリストに追加済みの時
                #     if current.back is None: #さらに現在のノードがルートであるとき
                #         flag = False #すべての値の追加が完了したのでflagをFalseに
                #         break
                #     current = current.back # 1つ前のノードに戻る
            current = current.right # 右に移る
        return result



rndArray = [5, 8, 2, 3, 4, 7, 1, 9, 4, 6]
tree = Tree()
for i in rndArray:
    tree.insert(i)
print(tree.printlist())

# print(tree.root.value)
# print(tree.root.left.value)
# print(tree.root.left.left.value)
# # print(tree.root.left.left.left.value)
# print(tree.root.left.right.value)
# print(tree.root.left.right.right.value)
# # print(tree.root.left.right.right.right.value)
# print(tree.root.left.right.right.left.value)
# # print(tree.root.left.right.left.value)
# print(tree.root.right.value)
# print(tree.root.right.left.left.value)





