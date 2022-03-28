import const

# 需要生成的职业, 按照套装顺序填入列表, 需要忽略的使用下划线_填充
gs = [
    # 坦克
    "PLD",  # 骑士
    "WAR",  # 战士
    "DRK",  # 暗黑骑士
    "GNB",  # 绝枪战士

    # 治疗
    "WHM",  # 白魔法师
    "SCH",  # 学者
    "AST",  # 占星术士
    "SGE",  # 贤者

    # 近战
    "MNK",  # 武僧
    "DRG",  # 龙骑士
    "NIN",  # 忍者
    "SAM",  # 武士
    "RPR",  # 钐镰客

    # 远敏
    "BRD",  # 吟游诗人
    "MCH",  # 机工士
    "DNC",  # 舞者

    # 法师
    "BLM",  # 黑魔法师
    "SMN",  # 召唤师
    "RDM",  # 赤魔法师
    "BLU",  # 青魔法师

    # 生产
    "CRP",  # 刻木匠
    "BSM",  # 锻铁匠
    "ARM",  # 铸甲匠
    "GSM",  # 雕金匠
    "LTW",  # 制革匠
    "WVR",  # 裁衣匠
    "ALC",  # 炼金术士
    "CUL",  # 烹调师

    # 采集
    "MIN",  # 采矿工
    "BTN",  # 园艺工
    "FSH",  # 捕鱼人
]

# 设置每个职能共享技能栏
# [("来源快捷栏职业", 来源快捷栏id, 目标职业快捷栏id)]
share_hotbar = {
    const.CLASS_TYPE_TANK: [("GLA", 4, 4)],
    const.CLASS_TYPE_HEALER: [("CNJ", 4, 4)],
    const.CLASS_TYPE_MELEE: [("PGL", 4, 4)],
    const.CLASS_TYPE_PHYSICAL_RANGED: [("ARC", 4, 4)],
    const.CLASS_TYPE_MAGICAL_RANGED: [("THM", 4, 4)],
    const.CLASS_TYPE_HAND: [("CRP", 1, 1),("CRP", 2, 2),("CRP", 3, 3)],
}