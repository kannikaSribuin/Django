from django import forms

class ProductForm(forms.Form):
    NAME_LIST = [('JACQUEMUS', 'JACQUEMUS'),
                  ('PRADA Re-Nylon', 'PRADA Re-Nylon'),
                  ('Chanel', 'Chanel'),
                  ('BURBERRY', 'BURBERRY'),
                  ('Gucci', 'Gucci'),
                  ]
    COLOR_LIST = [('White', 'White'),
                  ('Black', 'black'),
                  ('Gary', 'Gary'),
                  ('Brown', 'Brown'),
                  ('Cream', 'Cream'),
                  ('Silver', 'Silver'),
                  ]
    TYPE_LIST = [('Top Hat', 'Top Hat'),
                 ('Bowler', 'Bowler'),
                 ('Homburg', 'Homburg'),
                 ('Porkpie', 'Porkpie'),
                 ('Cloche', 'Cloche')
                 ]
    SIZE_list = [('S', 'S'),
                 ('M', 'M'),
                 ('L', 'L'),
                 ]
    id = forms.CharField(max_length=13, label= "รหัสสินค้า",
                         required=True, widget=forms.TextInput(attrs={'size': '15'}))
    name = forms.CharField(max_length=30, label="ชื่อ", required=True, widget=forms.Select(choices=NAME_LIST))
    color = forms.CharField(max_length=30, label="สี", required=True, widget=forms.Select(choices=COLOR_LIST))
    price = forms.IntegerField(label="ราคา", required=True, widget=forms.NumberInput)
    amount = forms.IntegerField(label= "จำนวน", required=True,widget=forms.NumberInput)
    size = forms.CharField(label= 'ขนาด', required=True, widget=forms.RadioSelect(choices=SIZE_list))


