from re import S
import re
from rest_framework import serializers
from ..models import Artist, Album, Track

class AlbumListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'name',)

class AlbumSerializer(serializers.ModelSerializer):
    
    class ArtistSerializer(serializers.ModelSerializer):
        class Meta:
            model = Artist
            fields = ('id', 'name',)
    
    class TrackSerializer(serializers.ModelSerializer):
        class Meta:
            model = Track
            fields = ('id', 'title',)

    name = serializers.CharField(min_length=2, max_length=100)
    artists = ArtistSerializer(many=True, read_only=True)
    tracks = TrackSerializer(many=True, read_only=True)

    artist_pks = serializers.ListField(write_only=True)

    def create(self, validated_data):
        artist_pks = validated_data.pop('artist_pks')
        album = Album.objects.create(**validated_data)

        for artist_pk in artist_pks:
            album.artists.add(artist_pk)
        
        return album

    def update(self, album, validated_data):
        artist_pks = validated_data.pop('artist_pks')

        for attr, value in validated_data.items():
            setattr(album, attr, value)
            album.save()
        
        album.artists.clear()

        for artist_pk in artist_pks:
            album.artists.add(artist_pk)

        return album


    class Meta:
        model = Album
        fields = ('id', 'name', 'artists', 'tracks', 'artist_pks',)