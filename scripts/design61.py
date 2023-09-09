import gradio as gr 
import os 
import re 
import shutil 
from modules import scripts ,sd_models ,script_callbacks ,errors 
from modules .ui_components import InputAccordion 
from modules .shared import opts ,cmd_opts 
OOO000000OOO00OO0 ={"txt2img":False ,"img2img":False ,"same":False }
class O0000000O0OOOOO00 (scripts .ScriptBuiltinUI ):
    section ="accordions"
    create_group =False 
    def __init__ (OO0000O0000OOOO0O ):
        pass 
    def title (OO0O000OO0O000000 ):
        return "output-path-helper"
    def show (O000OOO0OOOOOO0O0 ,OO00O000OO00OO00O ):
        return scripts .AlwaysVisible 
    def ui (OOO00OOOOOOOO0000 ,OO0OO000OO0O00000 ):
        def O0O00O0OOO00O0O0O (O0O00O0OOO00O0O00 ):
            global OOO000000OOO00OO0 
            OOO000000OOO00OO0 ["img2img"if OO0OO000OO0O00000 else "txt2img"]=O0O00O0OOO00O0O00 
        with InputAccordion (False ,label =f"保存到 {'图生图' if OO0OO000OO0O00000 else '文生图'} 子路径",elem_id =OOO00OOOOOOOO0000 .elem_id ("project_name_box"))as O0O0OOO0OOO0OOOOO :
            with gr .Column ():
                O000O0O0O0O0000O0 =gr .Dropdown (OO0O0OO00O00O0OOO (OO0OO000OO0O00000 ),show_label =False ,allow_custom_value =True ,info ="输入格式 文件夹名 或 文件夹名/文件夹名")
                O000O0O0O0O0000O0 .change (fn =O0O00O0OOO00O0O0O ,inputs =[O000O0O0O0O0000O0 ])
                if OO0OO000OO0O00000 :
                    O000O0O0O0O0000O0 .blur (fn =OOO00O0OO00O00000 ,outputs =[O000O0O0O0O0000O0 ])
                else :
                    O000O0O0O0O0000O0 .blur (fn =OOO0OO0OO0O000OOO ,outputs =[O000O0O0O0O0000O0 ])
        return O0O0OOO0OOO0OOOOO ,O000O0O0O0O0000O0 
def OO0O0OO00O00O0OOO (O000OO00OOO0OOO0O ):
    if O000OO00OOO0OOO0O :
        O0O000O0O000OOO00 =opts .outdir_samples or opts .outdir_img2img_samples 
    else :
        O0O000O0O000OOO00 =opts .outdir_samples or opts .outdir_txt2img_samples 
    OO00OO00O0O00O000 =O0OO0O0O00OO0O0O0 (O0O000O0O000OOO00 ,[],O0O000O0O000OOO00 )
    return OO00OO00O0O00O000 
def O0OO0O0O00OO0O0O0 (OOOO0O00O0OOO000O ,O0O0O000OO0000O00 ,OO00O000OOOOOOO0O =False ):
    for OOO0O0OOOOOO0OOOO in os .listdir (OOOO0O00O0OOO000O ):
        O00OOO000000000OO =os .path .join (OOOO0O00O0OOO000O ,OOO0O0OOOOOO0OOOO ).replace ('\\','/')
        if os .path .isdir (O00OOO000000000OO ):
            O0O0O000OO0000O00 .append (O00OOO000000000OO .split (f"{OO00O000OOOOOOO0O}/")[1 ])
            O0OO0O0O00OO0O0O0 (O00OOO000000000OO ,O0O0O000OO0000O00 ,OO00O000OOOOOOO0O )
    return O0O0O000OO0000O00 
def OOO00O0OO00O00000 ():
    return gr .update (choices =OO0O0OO00O00O0OOO (True ))
def OOO0OO0OO0O000OOO ():
    return gr .update (choices =OO0O0OO00O00O0OOO (False ))
def O0000OOO0OOOOOOOO (O000000000OOO0O00 ):
    O0OO0000OOO0OO0O0 ,_O0OO00OO00OOO0O0O =os .path .splitext (O000000000OOO0O00 )
    O00OOO0O00OOO000O =O0OO0000OOO0OO0O0 +'.txt'
    return O00OOO0O00OOO000O 
def O0OOOOO0OOOO0O000 (OOOO0OOOO0O0OOO00 :script_callbacks .ImageSaveParams ):
    global OOO000000OOO00OO0 
    O0O0O0OOOO00O0O0O =re .search (r'[\/\\]img2img',OOOO0OOOO0O0OOO00 .filename )
    OOO0000O00OO0OOO0 =OOO000000OOO00OO0 ["img2img"if O0O0O0OOOO00O0O0O else "txt2img"]
    print (O0O0O0OOOO00O0O0O )
    print (OOO0000O00OO0OOO0 )
    if OOO0000O00OO0OOO0 ==False or "grid"in OOOO0OOOO0O0OOO00 .filename :
        return 
    O0OO0O0OOO00O0OOO =OOOO0OOOO0O0OOO00 .filename 
    if O0OO0O0OOO00O0OOO is not None and os .path .exists (O0OO0O0OOO00O0OOO ):
        OOO0O0OO0O000000O =os .path .split (O0OO0O0OOO00O0OOO )[0 ]
        OO00O0OO0O00OOOOO =os .path .join (OOO0O0OO0O000000O ,OOO0000O00OO0OOO0 )
        if not os .path .exists (OO00O0OO0O00OOOOO ):
            os .makedirs (OO00O0OO0O00OOOOO )
        O00OOO00OO00O0O0O (O0OO0O0OOO00O0OOO ,OO00O0OO0O00OOOOO )
script_callbacks .on_image_saved (O0OOOOO0OOOO0O000 )
def O00OOO00OO00O0O0O (OO000OO0O0OO00000 ,OOO0OO00O00OO0000 ):
    def O0O00OO000OO0000O (OO00OO0OOO00000O0 ,OOOOO00OO0OOOOO00 ):
        OOO000O00O0O00O00 ,OOOOOO00O000OO0OO =os .path .splitext (OO00OO0OOO00000O0 )
        O0000O00O0O000000 =os .listdir (OOOOO00OO0OOOOO00 )
        O000OO00O000O000O =0 
        for O0O0O00000000O0O0 in O0000O00O0O000000 :
            if len (O0O0O00000000O0O0 )<=len (OO00OO0OOO00000O0 ):
                continue 
            O0OOOO0O0O0OOO0OO =O0O0O00000000O0O0 [-len (OOOOOO00O000OO0OO ):]if len (OOOOOO00O000OO0OO )>0 else ""
            if O0O0O00000000O0O0 [:len (OOO000O00O0O00O00 )]==OOO000O00O0O00O00 and O0OOOO0O0O0OOO0OO ==OOOOOO00O000OO0OO :
                if O0O0O00000000O0O0 [len (OOO000O00O0O00O00 )]=="("and O0O0O00000000O0O0 [-len (OOOOOO00O000OO0OO )-1 ]==")":
                    OOOO0O0O00O00OOOO =O0O0O00000000O0O0 [len (OOO000O00O0O00O00 )+1 :-len (OOOOOO00O000OO0OO )-1 ]
                    if OOOO0O0O00O00OOOO .isdigit ():
                        if int (OOOO0O0O00O00OOOO )>O000OO00O000O000O :
                            O000OO00O000O000O =int (OOOO0O0O00O00OOOO )
        return f"{OOO000O00O0O00O00}({O000OO00O000O000O + 1}){OOOOOO00O000OO0OO}"
    O00O000OO00OO0OO0 =os .path .basename (OO000OO0O0OO00000 )
    OOO000000OO000OOO =os .path .join (OOO0OO00O00OO0000 ,O00O000OO00OO0OO0 )
    O0OOOOO00OOOOO00O =False 
    if opts .image_browser_txt_files :
        O0000OOO0O0O0OOO0 =O0000OOO0OOOOOOOO (OO000OO0O0OO00000 )
        if os .path .exists (O0000OOO0O0O0OOO0 ):
            O0OOOOO00OOOOO00O =True 
    if not os .path .exists (OOO000000OO000OOO ):
        if opts .image_browser_copy_image :
            shutil .copy2 (OO000OO0O0OO00000 ,OOO0OO00O00OO0000 )
            if opts .image_browser_txt_files and O0OOOOO00OOOOO00O :
                shutil .copy2 (O0000OOO0O0O0OOO0 ,OOO0OO00O00OO0000 )
        else :
            shutil .move (OO000OO0O0OO00000 ,OOO0OO00O00OO0000 )
            if opts .image_browser_txt_files and O0OOOOO00OOOOO00O :
                shutil .move (O0000OOO0O0O0OOO0 ,OOO0OO00O00OO0000 )
    else :
        O00O000OO00OO0OO0 =O0O00OO000OO0000O (O00O000OO00OO0OO0 ,OOO0OO00O00OO0000 )
        if opts .image_browser_copy_image :
            shutil .copy2 (OO000OO0O0OO00000 ,os .path .join (OOO0OO00O00OO0000 ,O00O000OO00OO0OO0 ))
            if opts .image_browser_txt_files and O0OOOOO00OOOOO00O :
                shutil .copy2 (O0000OOO0O0O0OOO0 ,O0000OOO0OOOOOOOO (os .path .join (OOO0OO00O00OO0000 ,O00O000OO00OO0OO0 )))
        else :
            shutil .move (OO000OO0O0OO00000 ,os .path .join (OOO0OO00O00OO0000 ,O00O000OO00OO0OO0 ))
            if opts .image_browser_txt_files and O0OOOOO00OOOOO00O :
                shutil .move (O0000OOO0O0O0OOO0 ,O0000OOO0OOOOOOOO (os .path .join (OOO0OO00O00OO0000 ,O00O000OO00OO0OO0 )))
