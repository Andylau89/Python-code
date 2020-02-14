import sys

sys.path.append('C:/Users/Administrator/PycharmProjects/my_project_exercise')
# print(sys.path)

import skill_system.skill_deployer as skill_deployer
from common.double_list_helper import *

print(skill_deployer.skill_deployer)


class SkillData:
    def get_skills(self):
        print('获取技能')


DoubleHelper.get_element()
DoubleHelper().get_element1()
print("It's skilldata module")
