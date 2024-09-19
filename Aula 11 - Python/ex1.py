dic_emoji = {
    ':)':'🙂',
    ':(':'☹',
    ';)':'😉',
    "'-'":'😐',
    'carioba':'🥶🤠'
}
frase = ':)'

for key in dic_emoji.keys():
    frase = frase.replace(key,dic_emoji[key])
frase.replace('','')
print(frase)