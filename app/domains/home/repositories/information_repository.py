from app.domains.home.models.home_information import HomeInformation



class HomeInformationRepository():
    async def save_information(self, information:HomeInformation):
        self.session.add(information)