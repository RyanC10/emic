from django import forms
from django.template.defaultfilters import mark_safe
import datetime


class FormaTEXT(forms.Form):
    mjerenje_1 = forms.CharField(max_length = 3,label=mark_safe('<strong>1. Kako se zove Adamovi Evin sin koji se rodio nakon smrti Abela? </strong>'), initial='_ _ _')
    mjerenje_2 = forms.CharField(max_length = 10,label=mark_safe('<strong>2. Najstariji čovjek koji se spominje u Bibliji?</strong>'), initial='_ _ _ _ _ _ _ _ _')
    mjerenje_3 = forms.CharField(max_length = 5,label=mark_safe('<strong>3. Koga je Bog živog uzeo sa zemlje?</strong>'), initial='_ _ _ _ _')
    mjerenje_4 = forms.CharField(max_length = 2,label=mark_safe('<strong>4. Koliko dana je padala kiša pri velikom potopu?</strong>'), initial='_ _ _ _ _')
    mjerenje_5 = forms.CharField(max_length = 4,label=mark_safe('<strong>5. Znak saveza nakon potopa?</strong>'), initial='_ _ _ _ _')
    mjerenje_6 = forms.CharField(max_length = 3,label=mark_safe('<strong>6. Otac Šema,Hama,Jafeta?</strong>'), initial='_ _ _ _ _')
    mjerenje_7 = forms.CharField(max_length = 2,label=mark_safe('<strong>7. Iz kojeg je grada Abraham?</strong>'), initial='_ _ _ _ _')
    mjerenje_8 = forms.CharField(max_length = 10,label=mark_safe('<strong>8. Ko je blagoslovio Abrahama pri povratku iz boja?</strong>'), initial='_ _ _ _ _')
    mjerenje_9 = forms.CharField(max_length = 3,label=mark_safe('<strong>9. Koliko godina je Abraham živio? </strong>'), initial='_ _ _ _ _')
    mjerenje_11 = forms.CharField(max_length = 6,label=mark_safe('<strong>10.Ime Izakovog prvorođenca?</strong>'), initial='_ _ _ _ _')
    mjerenje_12 = forms.CharField(max_length = 200,label=mark_safe('<strong>11.Koliko djece je imao Jakov?</strong>'), initial='_ _ _ _ _')
    mjerenje_13 = forms.CharField(max_length = 200,label=mark_safe('<strong>12. Kako se zvao najmlađi Jakovljev sin?<strong>'), initial='_ _ _ _ _')
    mjerenje_14 = forms.CharField(max_length = 200,label=mark_safe('<strong>13. Koliko su godina Izraelci morali biti u Egiptu?</strong>'), initial='_ _ _ _ _')
    mjerenje_15 = forms.CharField(max_length = 200,label=mark_safe('<strong>14.Ime bogataša iz Arabije koji je preživio teške patnje?</strong>'), initial='_ _ _ _ _')
    mjerenje_16 = forms.CharField(max_length = 200,label=mark_safe('<strong>15. Aronov brat</strong>'), initial='_ _ _ _ _')
    mjerenje_17 = forms.CharField(max_length = 200,label=mark_safe('<strong>16.Kako se zove brdo na kojem je Bog dao 10 zapovjedi?</strong>'), initial='_ _ _ _ _')
    mjerenje_18 = forms.CharField(max_length = 200,label=mark_safe('<strong>17.Svećeničko pleme?</strong>'), initial='_ _ _ _ _')
    mjerenje_19 = forms.CharField(max_length = 200,label=mark_safe('<strong>18. Čiji je štap procvatao?(nominativ)</strong>'), initial='_ _ _ _ _')
    mjerenje_20 = forms.CharField(max_length = 200,label=mark_safe('<strong>19.Koliko su godina Izraelci bili u pustinji?</strong>'), initial='_ _ _ _ _')
    mjerenje_21 = forms.CharField(max_length = 200,label=mark_safe('<strong>20. Tko je uveo Izraelce u obećanu zemlju?</strong>'), initial='_ _ _ _ _')
    mjerenje_22 = forms.CharField(max_length = 200,label=mark_safe('<strong>21.Zidine kojeg su grada pale pod zvukom truba?</strong>'), initial='_ _ _ _ _')
    mjerenje_23 = forms.CharField(max_length = 200,label=mark_safe('<strong>22. Tko je odrezao kosu Samsonu?</strong>'), initial='_ _ _ _ _')
    mjerenje_24 = forms.CharField(max_length = 200,label=mark_safe('<strong>23.Tko je prvi rekao: Bože moj, zašto si me ostavio?</strong>'), initial='_ _ _ _ _')
    mjerenje_25 = forms.CharField(max_length = 200,label=mark_safe('<strong>24. Ime žene s kojom je sagriješio drugi kralj Izraela?</strong>'), initial='_ _ _ _ _')
    mjerenje_26 = forms.CharField(max_length = 200,label=mark_safe('<strong>25. Treći kralj izraela? Mudar na početku..., hram..?</strong>'), initial='_ _ _ _ _')
    mjerenje_27 = forms.CharField(max_length = 200,label=mark_safe('<strong>26. Zaustavio kišu i ponovo je vratio nakon 3 godine</strong>'), initial='_ _ _ _ _')
    mjerenje_28 = forms.CharField(max_length = 200,label=mark_safe('<strong>27.Koji prorok plače pred razvalinama Jeruzalema?</strong>'), initial='_ _ _ _ _')
    mjerenje_29 = forms.CharField(max_length = 200,label=mark_safe('<strong>28.Tko je prorokovao da će se roditi dijete kojem će ime biti Emanuel?</strong>'), initial='_ _ _ _ _')
    
    
  