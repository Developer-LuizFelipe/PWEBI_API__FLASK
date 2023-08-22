from flask_restful import Resource, reqparse
from flask import jsonify 
from models import db, Tutor, Pet, TutorSchema, PetSchema

class TutorResource(Resource):
    def get(self, tutor_id=None):
        if tutor_id is None:
            tutors = Tutor.query.all() 
            return TutorSchema(many=True).dump(tutors), 200
    
        tutor = Tutor.query.get(tutor_id)
        return TutorSchema().dump (tutor), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nome_tutor', type=str, required=True)
        args= parser.parse_args()
        tutor = Tutor (nome=args['nome_tutor'])
        db.session.add(tutor)
        db.session.commit()
        return TutorSchema().dump(tutor), 201
        
    def put(self, tutor_id):
        parser = reqparse.RequestParser()
        parser.add_argument('nome_tutor', type=str, required=True)
        args= parser.parse_args()
        tutor = Tutor.query.get(tutor_id)
        tutor.nome = args['nome_tutor']
        db.session.commit()
        return TutorSchema().dump(tutor), 200
    
    def delete(self, tutor_id):
        tutor = Tutor.query.get(tutor_id)
        db.session.delete(tutor)
        db.session.commit()
        return jsonify({"msg":"Tutor Excluido !"})
    
class PetResource(Resource):
    def get(self, pet_id):
        pet = Pet.query.get(pet_id)
        return PetSchema().dump(pet), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nome_pet', type=str, required=True)
        parser.add_argument('tutor_id', type=int, required=True)
        args= parser.parse_args()
        pet = Pet (nome=args['nome_pet'], tutor_id=args['tutor_id'])
        db.session.add(pet)
        db.session.commit()
        return PetSchema().dump(pet), 201
    
    def put(self, pet_id):
        parser = reqparse.RequestParser()
        parser.add_argument('nome_pet', type=str, required=True)
        parser.add_argument('tutor_id', type=int, required=True)
        args= parser.parse_args()
        pet = Pet.query.get(pet_id)
        pet.nome = args['nome_pet']
        pet.tutor_id = args['tutor_id']
        db.session.commit()
        return PetSchema().dump(pet), 200
    
    def delete(self, pet_id):
        pet = Pet.query.get(pet_id)
        db.session.delete(pet)
        db.session.commit()
        return jsonify({"msg":"Pet excluido !"})
    