#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2021/06/04
"""

import random

# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��
computer = random.randint(0, 4)
user = int(input('���������ѡ��0.ʯͷ��1.ʷ���ˣ�2.ֽ��3.���棬4.����'))

def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

    if  computer == 0:
        computer = 'ʯͷ'
    elif computer == 1:
         computer = 'ʷ����'
    elif computer == 2:
         computer = 'ֽ'
    elif computer == 3:
         computer = '����'
    elif computer == 4:
         computer = '����'
    else:
         print('Error: No Correct Name')


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    if user == 'ʯͷ':
       user = 0
    elif user == 'ʷ����':
         user = 1
    elif user == 'ֽ':
         user = 2
    elif user == '����':
         user = 3
    else:
         user = '����'
    print('�����˳�����:%s,�û�������:%s' % (computer, user))
if ((user == 0 and computer == 3 or 4)
           or (user == 1 and computer == 0 or 4)
           or (user == 2 and computer == 1 or 0)
           or (user == 3 and computer == 1 or 2)
           or (user == 4 and computer == 3 or 2)):
       print('��Ӯ��')
elif user == computer:
      print('ƽ��')
else:
      print('����Ӯ��')

    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

   




