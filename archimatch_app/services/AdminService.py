from archimatch_app.serializers import AdminSerializer
from archimatch_app.serializers.utils.ArchiReportSerializer import ArchiReportSerializer
from archimatch_app.serializers.utils.ClientReportSerializer import ClientReportSerializer
from archimatch_app.serializers.utils.CommentReportSerializer import CommentReportSerializer
from archimatch_app.models.utils.Report import Report
from archimatch_app.serializers.utils.ReportsSerializer import ReportSerializer
from rest_framework.response import Response
from rest_framework import status
from archimatch_app.models import Admin,ArchimatchUser,Right,CommentReport
from django.contrib.auth.hashers import make_password
from archimatch_app.models.Selection import Selection
from archimatch_app.models.utils.ArchiReport import ArchiReport
from archimatch_app.models.utils.ClientReport import ClientReport
class AdminService:
    serializer_class = AdminSerializer
    archireport_class = ArchiReportSerializer
    clientreport_class = ClientReportSerializer

    commentReport_class = CommentReportSerializer

    report_class = ReportSerializer
    @classmethod
    def process_rights(self, rights):
        handled_rights = []
        for right in rights:
            existing_right = Right.objects.filter(display=right).first()  # Get first existing right
            if existing_right:
                handled_rights.append(existing_right.id)
            else:
                new_right = Right.objects.create(display=right, abbreviation="aa")
                handled_rights.append(new_right.id)
        return handled_rights
    

    def admin_create(self,request):
        data = request.data
        rights = data.get('rights',[])
        user_data = data.get("user")
        handled_rights= self.process_rights(rights)

        if ArchimatchUser.objects.filter(email=user_data["email"]).exists():
            return Response({"message": "email existe deja"}, status=status.HTTP_400_BAD_REQUEST)
        
        new_user = ArchimatchUser.objects.create(username=user_data["email"], first_name=user_data["first_name"],email=user_data["email"], password=make_password(user_data["password"]))
        admin = Admin.objects.create(user=new_user,super_user=False)  
        admin.rights.add(*handled_rights)  
        admin.save()

        response_data = {
            'message': 'Object created successfully with custom status code',
            
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
   
   
    def prolonger_selection(self,request):
        data = request.data
        print(data)
        date = data.get("date")
        id = data.get("id")
        selection = Selection.objects.filter(id=id).first()
        selection.expiration_date = date
        selection.save()
        response_data = {
            'message': 'Selection Prolonger',
            
        }
        return Response(response_data, status=status.HTTP_200_OK)
    


    def View_ArchiReports(self):
        archireports = ArchiReport.objects.all()
        serializer = self.archireport_class(archireports, many=True)
        response_data = {
            "message": "Architect reports found",
            "archireports": serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def View_ClientReports(self):
        clientreports = ClientReport.objects.all()
        serializer = self.clientreport_class(clientreports, many=True)
        response_data = {
            "message": "Architect reports found",
            "clientreports": serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)
    


    def view_reports(self):
        reports = Report.objects.all()
        serializer = self.report_class(reports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def view_archireports_descriptions(self,request,id):
        archireport = ArchiReport.objects.get(id=id)
        reports = archireport.reports.all()
        serializer = self.report_class(reports, many=True)
        response_data = {"message": "Archireport descriptions found!",
                         "descriptions": serializer.data}
        return Response(response_data, status=status.HTTP_200_OK)
    
    def view_clientreports_descriptions(self,request,id):
        clientrep = ClientReport.objects.get(id=id)
        reports = clientrep.reports.all()
        serializer = self.report_class(reports, many=True)
        response_data = {"message": "Archireport descriptions found!",
                         "descriptions": serializer.data}
        return Response(response_data, status=status.HTTP_200_OK)
    

    def View_CommentReport(self):
        archireports = CommentReport.objects.all()
        serializer = self.commentReport_class(archireports, many=True)
        response_data = {
            "message": "Architect reports found",
            "commentReports": serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def report_by_comment(self,request,id):
        commentReport = CommentReport.objects.get(id=id)
        reports = commentReport.reports.all()
        serializer = self.report_class(reports, many=True)
        response_data = {"message": "Archireport descriptions found!",
                         "descriptions": serializer.data}
        return Response(response_data, status=status.HTTP_200_OK)