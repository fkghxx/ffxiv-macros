# encoding=utf-8
import click
import const
import config
import macro
import os

output_path = "./"

class GS:
    job = ""
    gs_id = 0
    share_job = ""

    def __init__(self, job, gs_id) -> None:
        self.job = job
        self.gs_id = gs_id
        job_type = const.getJobType(job)
        if job_type == const.CLASS_TYPE_TANK:
            self.share_job = "GLA"
        elif job_type == const.CLASS_TYPE_HEALER:
            self.share_job = "CNJ"
        elif job_type == const.CLASS_TYPE_MELEE:
            self.share_job = "GLA"
        elif job_type == const.CLASS_TYPE_PHYSICAL_RANGED:
            self.share_job = "GLA"
        elif job_type == const.CLASS_TYPE_MAGICAL_RANGED:
            self.share_job = "GLA"
        elif job_type == const.CLASS_TYPE_HAND:
            self.share_job = "GLA"
        elif job_type == const.CLASS_TYPE_LAND:
            self.share_job = "GLA"


# 生成职业切换宏
def makeGsChangeMacros():
    gs_id = 0
    for job in config.gs:
        gs_id += 1
        job_type = const.getJobType(job)
        m = macro.Macro(job)
        m.add(macro.micon.icon(job, "classjob"))
        m.add(macro.gs.change(gs_id))

        if job_type in config.share_hotbar:
            for share_data in config.share_hotbar[job_type]:
                m.add(macro.hobar.copy(share_data[0], share_data[1], job, share_data[2]))
        job_path = f"{output_path}/{job_type}".replace("//", "/")
        m.toFile(job_path)
        
        


    

@click.command()
@click.option('-o', '--output', help='output path', required=False)
def main(output):
    global output_path
    output_path = "./"
    if output:
        output_path = output

    makeGsChangeMacros()

if __name__ == '__main__':

    main()
