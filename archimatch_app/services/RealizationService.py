from archimatch_app.serializers import RealizationSerializer
from archimatch_app.serializers.utils.RealizationImageSerializer import RealizationImageSerializer
from archimatch_app.serializers.utils.SubCategorySerializer import SubCategorySerializer

from rest_framework.response import Response
from rest_framework import status
from archimatch_app.models import Realization,RealizationImage,Architect,ArchimatchUser,Category,SubCategory



class RealizationService:
    serializer_class = RealizationSerializer
    realization_image_serializer_class = RealizationImageSerializer
    serializer_subcategory = SubCategorySerializer

    
    def category_process(self,category):
        filtered_instances = Category.objects.filter(display=category)
        instance = None
        if not filtered_instances.exists():
            instance = Category.objects.create(display=category)
        else:
            instance = filtered_instances.first()
           
        
        return instance
    
    def realization_create(self, request):
        # Get the user ID from the request data
        arch_id = request.data.get('id')
        # Retrieve the user and architect objects
        user = ArchimatchUser.objects.get(id=arch_id)
        architect = Architect.objects.filter(user=user).first()
        category = self.category_process(request.data.get('categories'))
        # Create a realization instance
        realization = Realization.objects.create(
            architect=architect,
            categorie=category,
            style=request.data.get('work_style'),
            city=request.data.get('town'),
            surface=request.data.get('surface_travaux'),
            service=request.data.get('need'),
            description=request.data.get('details'),
            project_title=request.data.get('project_title')
        )

        # Get the list of uploaded images
        images_data = request.FILES.getlist('images')
        
        # Create RealizationImage objects and save them
        images = []
        print(request.data)
        for image_data in images_data:
            print("image_data")
            print(image_data)
            image = RealizationImage(realization=realization, image=image_data)
            image.save()
            images.append(image)

        # Optionally, save the realization object
        realization.save()

        # Serialize the realization object
        serializer = self.serializer_class(realization)

        # Prepare response data
        response_data = {
            'message': 'Object created successfully',
            'realization': serializer.data
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

    
    def realizations_view(self,request,pk):
       
       data = request.data
       user = ArchimatchUser.objects.get(id=pk)
       architect = Architect.objects.filter(user=user).first()
       realizations = Realization.objects.filter(architect=architect)

       serializer = self.serializer_class(realizations,many=True)
       
       response_data = {
            'message': 'Objects found successfully',
            'realization': serializer.data
        }

       return Response(response_data, status=status.HTTP_200_OK)
    
    def realization_view(self,request,pk):
       
       realization = Realization.objects.filter(id=pk).first()
       print (realization)
       
       realization_serializer = self.serializer_class(realization,many=False)
       
       realization_images = RealizationImage.objects.filter(realization=realization)
       print(realization_images)
       realization_image_serializer = self.realization_image_serializer_class(realization_images, many=True)
       response_data = {
            'message': 'Object found successfully',
            'realization': realization_serializer.data,
            # 'images':realization_image_serializer.data,
        }

       return Response(response_data, status=status.HTTP_200_OK)
    
    def realization_update(self,request):
       data = request.data
       print("aaaaaaaaa",data)
       real_id = data.get('id')
       
       realization = Realization.objects.get(id=real_id)
       print (realization)
       realization.categorie = self.category_process(request.data.get('categories'))
       print(realization.categorie)
       realization.style = data.get('work_style')
       realization.city = data.get('town')
       realization.surface = data.get('surface_travaux')
       realization.service = data.get('need')
       realization.description = data.get('details')
        

       RealizationImage.objects.filter(realization=realization).delete()
       images_data = request.FILES.getlist('images')
       print(images_data)
       images = []
       if images_data:
           for image_data in images_data:
                image = RealizationImage(realization=realization, image=image_data)
                images.append(image)

       RealizationImage.objects.bulk_create(images)

       realization.save()
       serializer = self.serializer_class(realization)

       response_data = {
            'message': 'Object Updated successfully',
            'realization': serializer.data
        }

       return Response(response_data, status=status.HTTP_200_OK)



     

    def realization_delete(self,request):
       data = request.data
       print(data)
       real_id = data.get('id')
       realization = Realization.objects.get(id=real_id)

       realization.delete()

       response_data = {
            'message': 'Object Deleted successfully'        }

       return Response(response_data, status=status.HTTP_200_OK)
    

    # View Sub-Categories
    def View_SubCategories(self,category_name):
       print(category_name)
       category = Category.objects.filter(display=category_name).first()
       print(category)
       sub_categories = category.sub_categories.all()       
       serializer = self.serializer_subcategory(sub_categories, many=True)


       response_data = {
            'message': 'Subcategories retrieved successfully', 
            'Sub_categories': serializer.data       }

       return Response(response_data, status=status.HTTP_200_OK)
    
    # View Realization selon Category
    def View_RealizationPerCategory(self,category_name):
       category = Category.objects.filter(display=category_name).first()
       print(category)
       realizations = Realization.objects.filter(categorie=category)  
       print(realizations)
       serializer = self.serializer_class(realizations, many=True)


       response_data = {
            'message': 'Realizations retrieved successfully', 
            'realizations': serializer.data       }

       return Response(response_data, status=status.HTTP_200_OK)