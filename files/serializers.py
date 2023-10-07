from rest_framework import serializers

from files.models import File


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = [
            'id',
            'user',
            'title',
            'size',
            'upload_date',
            'download_last_date',
            'comment',
            'path',
            'download_link',
            'upload'
        ]
        read_only_fields = ['user', ]

    def perform_create(self, serializer):
        # print(validated_data)
        serializer.save(user=self.request.user)

    # def create(self, validated_data):
    #     print(validated_data)
    #     return super().create(validated_data)



        # title = models.CharField(max_length=128)
        # size = models.CharField()
        # upload_date = models.DateTimeField(auto_now_add=True)
        # download_last_date = models.DateTimeField()
        # comment = models.TextField()
        # path = models.CharField()
        # download_link = models.CharField()
        # upload = models.FileField()