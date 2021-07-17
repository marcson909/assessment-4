from craig_app.models import *

# drop everything first
Category.objects.all().delete()
Post.objects.all().delete()

c1 = Category.objects.create(name="Community")
c1.save()
c1s = Category.objects.create(name="Volunteers", parent=c1)
c1s.save()

c2 = Category.objects.create(name="Housing")
c2.save()
c2s = Category.objects.create(name="Apts/Housing", parent=c2)
c2s.save()
c2s2 = Category.objects.create(name="Housing Wanted", parent=c2)
c2s2.save()

p1 = Post.objects.create(title='Humane Society Volunteers needed', description="We need 3 volunteers at the humane society next weekend at 2pm for roughly 1 hour to help walk dogs", category=c1s)
p1.save()

p2 = Post.objects.create(title='Looking for 2br apt', description="Looking for 2br apt within walking distance of downtown", category=c2s2)
p2.save()

