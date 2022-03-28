CLASS_TYPE_TANK = "tank"
CLASS_TYPE_HEALER = "healer"
CLASS_TYPE_MELEE = "melee"
CLASS_TYPE_PHYSICAL_RANGED = "physical_ranged"
CLASS_TYPE_MAGICAL_RANGED = "magical_ranged"
CLASS_TYPE_HAND = "hand"
CLASS_TYPE_LAND = "land"

_jobs = [
    # 坦克
    "PLD",  # 骑士
    "WAR",  # 战士
    "DRK",  # 暗黑骑士
    "GNB",  # 绝枪战士
    "_tank_max",

    # 治疗
    "WHM",  # 白魔法师
    "SCH",  # 学者
    "AST",  # 占星术士
    "SGE",  # 贤者
    "_healer_max",

    # 近战
    "MNK",  # 武僧
    "DRG",  # 龙骑士
    "NIN",  # 忍者
    "SAM",  # 武士
    "RPR",  # 钐镰客
    "_melee_max",

    # 远敏
    "BRD",  # 吟游诗人
    "MCH",  # 机工士
    "DNC",  # 舞者
    "_physical_ranged_max",

    # 法师
    "BLM",  # 黑魔法师
    "SMN",  # 召唤师
    "RDM",  # 赤魔法师
    "BLU",  # 青魔法师
    "_magical_ranged_max",

    # 生产
    "CRP",  # 刻木匠
    "BSM",  # 锻铁匠
    "ARM",  # 铸甲匠
    "GSM",  # 雕金匠
    "LTW",  # 制革匠
    "WVR",  # 裁衣匠
    "ALC",  # 炼金术士
    "CUL",  # 烹调师
    "_hand_max",

    # 采集
    "MIN",  # 采矿工
    "BTN",  # 园艺工
    "FSH",  # 捕鱼人
    "_land_max",
]

# 获得特职的职能分类
def getJobType(job) -> str:
    job_index = _jobs.index(job)
    start, end = 0, _jobs.index("_tank_max")
    if start <= job_index < end:
        return CLASS_TYPE_TANK
    start, end = end, _jobs.index("_healer_max")
    if start < job_index < end:
        return CLASS_TYPE_HEALER
    start, end = end, _jobs.index("_melee_max")
    if start < job_index < end:
        return CLASS_TYPE_MELEE
    start, end = end, _jobs.index("_physical_ranged_max")
    if start < job_index < end:
        return CLASS_TYPE_PHYSICAL_RANGED
    start, end = end, _jobs.index("_magical_ranged_max")
    if start < job_index < end:
        return CLASS_TYPE_MAGICAL_RANGED
    start, end = end, _jobs.index("_hand_max")
    if start < job_index < end:
        return CLASS_TYPE_HAND
    start, end = end, _jobs.index("_land_max")
    if start < job_index < end:
        return CLASS_TYPE_LAND
    return ""