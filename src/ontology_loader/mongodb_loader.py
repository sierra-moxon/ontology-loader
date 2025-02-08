from linkml_store import Client
import logging
from linkml_runtime import SchemaView

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class MongoDBLoader:
    def __init__(self, schema_view: SchemaView):
        """
        Initialize MongoDB using LinkML-store's client.

        :param schema_view: LinkML SchemaView for ontology
        """
        self.client = Client()
        self.db = self.client.attach_database("mongodb", alias="nmdc", schema_view=schema_view)

    def insert_ontology_classes(self, ontology_classes):
        """
        Insert each OntologyClass object into the 'ontology_class_set' collection.

        :param ontology_classes: A list of OntologyClass objects to insert
        """
        collection = self.db.create_collection("ontology_class_set", recreate_if_exists=True)

        if ontology_classes:
            collection.insert(ontology_classes)
            logging.info(f"Inserted {len(ontology_classes)} OntologyClass objects into MongoDB.")
        else:
            logging.info("No OntologyClass objects to insert.")

    def insert_ontology_relations(self, ontology_relations):
        """
        Insert each OntologyClass object into the 'ontology_class_set' collection.

        :param ontology_relations: A list of OntologyClass objects to insert
        """
        collection = self.db.create_collection("ontology_relation_set", recreate_if_exists=True)

        if ontology_relations:
            collection.insert(ontology_relations)
            logging.info(f"Inserted {len(ontology_relations)} OntologyRelations objects into MongoDB.")
        else:
            logging.info("No OntologyRelation objects to insert.")