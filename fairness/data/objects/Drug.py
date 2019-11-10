from fairness.data.objects.Data import Data

class Drug(Data):

    def __init__(self):
        Data.__init__(self)

        self.dataset_name = 'drug'
        self.class_attr = 'Heroin'
        self.positive_class_val = 1
        self.sensitive_attrs = ['Gender']
        self.privileged_class_names = [1]
        self.categorical_features = []
        self.features_to_keep = ["Age","Gender","Education", "Country","Ethnicity", "Nscore", "Escore", "Oscore", "Ascore","Cscore", "Impulsive", "SS", "Heroin"]
        self.missing_val_indicators = []
