from django import forms
from django.template.defaultfilters import mark_safe
import datetime


class FormaTEXT(forms.Form):
    mjerenje_1 = forms.CharField(max_length = 3,label=mark_safe('<strong>1. Kako se zove Adamovi Evin sin koji se rodio nakon smrti Abela? </strong>'))
    mjerenje_2 = forms.CharField(max_length = 10,label=mark_safe('<strong>2. Najstariji čovjek koji se spominje u Bibliji?</strong>'))
    mjerenje_3 = forms.CharField(max_length = 5,label=mark_safe('<strong>3. Koga je Bog živog uzeo sa zemlje?</strong>'))
    mjerenje_4 = forms.CharField(max_length = 2,label=mark_safe('<strong>4. Koliko dana je padala kiša pri velikom potopu?</strong>'))
    mjerenje_5 = forms.CharField(max_length = 4,label=mark_safe('<strong>5. Znak saveza nakon potopa?</strong>'))
    mjerenje_6 = forms.CharField(max_length = 3,label=mark_safe('<strong>6. Otac Šema,Hama,Jafeta?</strong>'))
    mjerenje_7 = forms.CharField(max_length = 2,label=mark_safe('<strong>7. Iz kojeg je grada Abraham?</strong>'))
    mjerenje_8 = forms.CharField(max_length = 10,label=mark_safe('<strong>8. Ko je blagoslovio Abrahama pri povratku iz boja?</strong>'))
    mjerenje_9 = forms.CharField(max_length = 3,label=mark_safe('<strong>9. Koliko godina je Abraham živio? </strong>'))
    mjerenje_11 = forms.CharField(max_length = 6,label=mark_safe('<strong>10.Ime Izakovog prvorođenca?</strong>'))
    mjerenje_12 = forms.CharField(max_length = 200,label=mark_safe('<strong>11.Koliko djece je imao Jakov?</strong>'))
    mjerenje_13 = forms.CharField(max_length = 200,label=mark_safe('<strong>12. Kako se zvao najmlađi Jakovljev sin?<strong>'))
    mjerenje_14 = forms.CharField(max_length = 200,label=mark_safe('<strong>13. Upravitelj cijelog Egipta, sin Jakovljev?</strong>'))
    mjerenje_15 = forms.CharField(max_length = 200,label=mark_safe('<strong>14.Bogataš iz Arabije koji je preživio teške patnje?</strong>'))
    mjerenje_16 = forms.CharField(max_length = 200,label=mark_safe('<strong>15. Aronov brat</strong>'))
    mjerenje_17 = forms.CharField(max_length = 200,label=mark_safe('<strong>16.Kako se zove brdo na kojem je Bog dao 10 zapovjedi?</strong>'))
    mjerenje_18 = forms.CharField(max_length = 200,label=mark_safe('<strong>17.Svećeničko pleme?</strong>'))
    mjerenje_19 = forms.CharField(max_length = 200,label=mark_safe('<strong>18. Čiji je štap procvatao?(nominativ)</strong>'))
    mjerenje_20 = forms.CharField(max_length = 200,label=mark_safe('<strong>19.Koliko su godina Izraelci bili u pustinji?</strong>'))
    mjerenje_21 = forms.CharField(max_length = 200,label=mark_safe('<strong>20. Tko je uveo Izraelce u obećanu zemlju?</strong>'))
    mjerenje_22 = forms.CharField(max_length = 200,label=mark_safe('<strong>21.Zidine kojeg su grada pale pod zvukom truba?</strong>'))
    mjerenje_23 = forms.CharField(max_length = 200,label=mark_safe('<strong>22. Tko je odrezao kosu Samsonu?</strong>'))
    mjerenje_24 = forms.CharField(max_length = 200,label=mark_safe('<strong>23.Tko je prvi rekao: Bože moj, zašto si me ostavio?</strong>'))
    mjerenje_25 = forms.CharField(max_length = 200,label=mark_safe('<strong>24. Ime žene s kojom je sagriješio drugi kralj Izraela?</strong>'))
    mjerenje_26 = forms.CharField(max_length = 200,label=mark_safe('<strong>25. Treći kralj izraela? Mudar na početku..., hram..?</strong>'))
    mjerenje_27 = forms.CharField(max_length = 200,label=mark_safe('<strong>26. Zaustavio kišu i ponovo je vratio nakon 3 godine</strong>'))
    mjerenje_28 = forms.CharField(max_length = 200,label=mark_safe('<strong>27.Koji prorok plače pred razvalinama Jeruzalema?</strong>'))
    mjerenje_29 = forms.CharField(max_length = 200,label=mark_safe('<strong>28.Dijete kojem će ime biti Emanuel?</strong>'))
