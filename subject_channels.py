# subject_channels.py
import discord
import json

# Define channels for subjects
# Uncomment before commit!!!!!
subjects_channels = {
    "ACCT": 1072400085264125952,
    "AESF": 1072400225286762566,
    "AIAA": 1072400253883514890,
    "AMAT": 1072400284619386953,
    "BIBU": 1072400300629049365,
    "BIEN": 1072400318790369301,
    "BIPH": 1129250201807355924,
    "BSBE": 1072400340877574176,
    "BTEC": 1072400363958837258,
    "CBME": 1072400415225806868,
    "CENG": 1072400525007528016,
    "CHEM": 1072402904562024488,
    "CHMS": 1072402932860981349,
    "CIEM": 1072402950393184317,
    "CIVL": 1072402970244829204,
    "CMAA": 1072402990306181240,
    "COMP": 1072403017804038185,
    "CORE": 1072403047260635146,
    "CPEG": 1072403065669431316,
    "CTDL": 1129252975970373682,
    "CSIC": 1072403105783742514,
    "CSIT": 1072403126981767218,
    "DASC": 1072403144484597761,
    "DBAP": 1072403162503315458,
    "DSAA": 1072403190122827817,
    "DSCT": 1072403208967823420,
    "ECON": 1072403243478556672,
    "EEMT": 1072403265515421726,
    "EESM": 1072403283571908658,
    "ELEC": 1072403304291770390,
    "EMIA": 1072403324164378684,
    "EMBA": 1091730890075410522,
    "ENEG": 1072403348965306418,
    "ENGG": 1072403566796472320,
    "ENTR": 1072403586690064445,
    "ENVR": 1072403614586388561,
    "ENVS": 1072403642205884446,
    "EOAS": 1072403665144512524,
    "EVNG": 1072403687365951538,
    "EVSM": 1072403708517830676,
    "FINA": 1072403736120528946,
    "FTEC": 1072403763740037160,
    "GBUS": 1072403790449360936,
    "GFIN": 1072403821734662155,
    "GNED": 1072403855490416700,
    "HART": 1129254031332753448,
    "HHMS": 1134390629829443684,
    "HLTH": 1072403882002620446,
    "HMAW": 1129255123714052198,
    "HMMA": 1072764384503418940,
    "HUMA": 1072764528523214928,
    "IBTM": 1072403908305109063,
    "IDPO": 1072403933424783431,
    "IEDA": 1072403955738493009,
    "IIMP": 1072403975741128774,
    "IROP": 1129255430263148574,
    "IMBA": 1091731206804078665,
    "INTR": 1072404006070128661,
    "IOTA": 1072404047715373056,
    "IPEN": 1072404065692155904,
    "ISDN": 1072404087884230676,
    "ISOM": 1072404108797034557,
    "JEVE": 1072404136395538492,
    "LABU": 1072404161804632095,
    "LANG": 1072404179273920533,
    "LEGL": 1129255684563796028,
    "LIFS": 1072404197301026888,
    "MAED": 1072404225390288938,
    "MAFS": 1072404251504025700,
    "MARK": 1072404283665961070,
    "MASS": 1072404311516119060,
    "MATH": 1072404403904053289,
    "MECH": 1072404428323303424,
    "MESF": 1072404460468449280,
    "MFIT": 1072404483381927957,
    "MGCS": 1072404512268111932,
    "MGMT": 1072404559877640223,
    "MICS": 1072404594992369726,
    "MILE": 1072404647840587836,
    "MIMT": 1072404676579954718,
    "MSBD": 1072404692862242878,
    "MSDM": 1072404736290066493,
    "MTLE": 1072404757349683320,
    "NANO": 1072404772461748264,
    "OCES": 1072404796679667722,
    "PDEV": 1072404820897562685,
    "PHYS": 1072404857761308712,
    "PPOL": 1072404878812532787,
    "RMBI": 1072404896898363432,
    "ROAS": 1072404923171471440,
    "SBMT": 1072404951965388870,
    "SCIE": 1072404969950560336,
    "SEEN": 1072404999826587748,
    "SHSS": 1072405035004207164,
    "SISP": 1129256253026222193,
    "SMMG": 1072405064746016819,
    "SOSC": 1072405103820148777,
    "SUST": 1072405123944431626,
    "TEMG": 1072405140205735986,
    "UCUG": 1129257006860083261,
    "UFUG": 1129257109691838524,
    "UGOD": 1072405165975539762,
    "UROP": 1072405199399948319,
    "WBBA": 1072405215178932254,
    "other": 1072780254306906112,
    "error": 1135779590443384872
}

# Uncomment when testing output
# Comment when commit!!!!!!!!!!
# subjects_channels = {
#     "ENGG": 1115147111974047744,
#     "MATH": 1115147149911531591,
#     "other": 1114416691649196032,
#     "error": 1135779590443384872
# }

async def find_channels(bot):
    channels = {k:await bot.fetch_channel(v) for k,v in subjects_channels.items()}
    return channels