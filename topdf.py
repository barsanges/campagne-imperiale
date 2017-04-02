import yaml
import argparse
import subprocess
import tempfile

if __name__ == "__main__":
    descr = 'turn a YAML character sheet for the role playing game '\
            '`Warhammer` to a PDF, using XeTeX in the process'
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument('fin', help='character sheet in YAML format')
    parser.add_argument('--tex-fout', default=None, help='name of the tex '\
                        'file to generate from `fin` (default is based on '\
                        'the name of the character)')
    parser.add_argument('--template', default='template.tex', help='XeTeX '\
                        'template to use (default is `template.tex`)')
    args = parser.parse_args()

    with open(args.fin, 'r', encoding='utf-8') as fin:
        content = yaml.load(fin)
    with open(args.template, 'r', encoding='utf-8') as template:
        sheet = template.read()

    if args.tex_fout is None:
        args.tex_fout = content['nom'] + ' - Caractéristiques.tex'

    for key in ('nom', 'carrière', 'blessures', 'destin', 'folie', 'xp', 'finances'):
        sheet = sheet.replace('<#%s>' % key, str(content[key]))

    sheet = sheet.replace('<#carrières_passées>', ', '.join(content['carrières_passées']))

    for key, values in content['caractéristiques'].items():
        for idx, value in enumerate(values):
            if idx == 1 and not value:
                value = ''
            elif idx == 1 and values[0] != values[2]:
                diff = values[2] - values[0]
                if diff > 9: # Compétence sur 100 et pas sur 10 (fragile)
                    diff = diff // 10 # Division entière
                value = '+' + str(value) + '\\up{%s}' % (diff * '*')
            elif idx == 1:
                value = '+' + str(value)
            else:
                value = str(value)
            sheet = sheet.replace('<#%s%d>' % (key, idx), value)

    for skill in content['compétences']:
        sheet = sheet.replace('<#compétence>', skill, 1)
    for skill in content['compétences_futures']:
        sheet = sheet.replace('<#compétence>', '\\emph{%s}' % skill, 1)
    sheet = sheet.replace('<#compétence>', '')

    for owned in content['possessions']:
        sheet = sheet.replace('<#possessions>', owned, 1)
    sheet = sheet.replace('<#possessions>', '')

    with open(args.tex_fout, 'w', encoding='utf-8') as fout:
        fout.write(sheet)

    with tempfile.TemporaryDirectory() as tmpdirname:
        subprocess.run(['xelatex', args.tex_fout, '-aux-directory=%s' % tmpdirname])
