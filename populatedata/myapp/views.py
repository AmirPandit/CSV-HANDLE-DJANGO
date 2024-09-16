import csv
import time
import logging
import chardet
from io import StringIO
from django.shortcuts import render
from django.db import transaction, IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book

@api_view(["POST"])
def uploadfunction(request):
    logger = logging.getLogger(__name__)

    if 'file' not in request.FILES:
        return Response({'Error': 'No file Provided'}, status=status.HTTP_400_BAD_REQUEST)
    
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        return Response({'Error':'Not CSV File Provided.'}, status=status.HTTP_400_BAD_REQUEST)
    
    file_content = csv_file.read()
    result = chardet.detect(file_content)
    encoding = result['encoding']
    csv_file.seek(0)

    try:
        file_content = file_content.decode(encoding)
    except UnicodeDecodeError as e:
        return Response({'Error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    reader = csv.DictReader(StringIO(file_content))

    starttime = time.time()
    books = []

    try:
        for row in reader:
            book = Book(
                title = row.get("Title"),
                author = row.get("Authors"),
                publisher = row.get("Publisher"),
                description = row.get("Description"),
                publish_date = row.get("Publish Date"),
                category = row.get("Category"),
            )
            books.append(book)

        with transaction.atomic():
            Book.objects.bulk_create(books)
        
        endtime = time.time()
        duration = endtime-starttime

        return Response({'message':f'file processed in{duration:.2f} seconds'}, status=status.HTTP_200_OK)
    
    except IntegrityError as ie:
        return Response({'Error': 'Database integrity error: ' + str(ie)}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        logger.error(f'Error occured:{e}')
        return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

def uploadfromhtml(request):
    return render(request, "index.html")