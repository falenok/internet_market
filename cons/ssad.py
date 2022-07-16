class Cup():
    type = models.CharField(max_length=200, default='1')
    color = models.CharField(max_length=200, default='Белый')
    surface = models.CharField(max_length=200, default='Гладкая')
    size = models.CharField(max_length=200, default='Большой')
    image = models.ImageField(upload_to='images', default='1_aLvXjS4.png')