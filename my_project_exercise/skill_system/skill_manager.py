from skill_system.skill_deployer import *
#下面只能从当前模块开始运行，才能成功导入
# from skill_deployer import *


class SkillManager:
    def create_skill(self):
        print('创建技能')
        SkillDeployer().generate_skill()


def skill_manager_fun01():
    print("It's a fun01 of skill_system --> skill_manager ")


def skill_manager_fun02():
    print("It's a fun02 of skill_system --> skill_manager ")


# print(__name__)
if __name__ == '__main__':
    skill_deployer_fun01()
    SkillDeployer().generate_skill()
