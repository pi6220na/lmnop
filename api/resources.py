# api/resources.py
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS, fields
from api.models import Artist, Venue, Show


class ArtistResource(ModelResource):
    class Meta:
        queryset = Artist.objects.all()
        limit = 0
        resource_name = 'artist'
        #filtering = {'name':ALL,}
        include_resource_uri = False

class VenueResource(ModelResource):
    class Meta:
        queryset = Venue.objects.all()
        limit = 0
        resource_name = 'venue'
        include_resource_uri = False

#     show_date = models.DateTimeField(blank=False)
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
#     venue = models.ForeignKey(Venue, on_delete=models.CASCADE)



class ShowResource(ModelResource):
    # artist = fields.ToOneField(ArtistResource, 'Artist', null=False, blank=True)  # was ForeignKey # ApiField works shouldn't use
    # venue = fields.ToOneField(VenueResource, 'Venue', null=False, blank=True)


    # this works, most likely way to go   shows id in uri:
    artist = fields.ToOneField(attribute="artist", to=ArtistResource)  # CharField worked # This works using ToOneField
    venue = fields.ToOneField(attribute="venue", to=VenueResource)

    # this works, shows translated foreign key value, not id
    # artist = fields.CharField(attribute="artist")
    # venue = fields.CharField(attribute="venue")

    class Meta:
        queryset = Show.objects.all()
        resource_name = 'show'
        fields = ['show_date', 'artist', 'venue']
        limit = 0
        include_resource_uri = False
