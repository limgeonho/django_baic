from django.db.models.fields import CharField
from rest_framework import serializers
from ..models import Artist, Album, Track

class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name',)

class ArtistSerializer(serializers.ModelSerializer):
    
    class TrackSerializer(serializers.ModelSerializer):
        class Meta:
            model = Track
            fields = ('id', 'title',)

    class AlbumSerializer(serializers.ModelSerializer):
        class Meta:
            model = Album
            fields = ('id', 'name',)

    name = serializers.CharField(min_length=1, max_length=100)
    albums = AlbumSerializer(many=True, read_only=True)
    tracks = TrackSerializer(many=True, read_only=True)
    # DB에는 없지만 새로운 필드이기 때문에 직접 생성...
    album_count = serializers.IntegerField(source='albums.count', read_only=True)
    
    class Meta:
        model = Artist
        fields = ('id', 'name', 'debut', 'albums', 'tracks', 'album_count',)
