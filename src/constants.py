url = 'https://www.personality-database.com'
weights_map = dict()

ena = ['FVLE', 'FLVE', 'EVLF', 'ELVF']
dio = ['LVFE', 'LFVE', 'EVFL', 'EFVL']
tria = ['VLFE', 'VFLE', 'ELFV', 'EFLV']
tessera = ['VFEL', 'VEFL', 'LFEV', 'LEFV']
pente = ['VLEF', 'VELF', 'FLEV', 'FELV']
exi = ['LVEF', 'LEVF', 'FVEL', 'FEVL']

attitudinal_psyche_categories = {
    'FVLE': ena, 'FLVE': ena, 'EVLF': ena, 'ELVF': ena,
    'LVFE': dio, 'LFVE': dio, 'EVFL': dio, 'EFVL': dio,
    'VLFE': tria, 'VFLE': tria, 'ELFV': tria, 'EFLV': tria,
    'VFEL': tessera, 'VEFL': tessera, 'LFEV': tessera, 'LEFV': tessera,
    'VLEF': pente, 'VELF': pente, 'FLEV': pente, 'FELV': pente,
    'LVEF': exi, 'LEVF': exi, 'FVEL': exi, 'FEVL': exi
}
