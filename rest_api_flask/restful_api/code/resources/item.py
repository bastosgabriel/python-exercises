from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from flask import jsonify

from models.item import ItemModel


class Items(Resource):

    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}, 200


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field is required!"
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="Every item needs a store id!"
                        )

    def get(self, name):
        if ItemModel.find_by_name(name):
            return {'item': ItemModel.find_by_name(name).json()}, 200
        else:
            return {'item': None}, 404

    @jwt_required()
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': f"An item named '{name}' already exists!"}, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])

        try:
            item.save_to_db()
        except Exception as err:
            return {"message": f"Could not insert the item: {err}"}, 500

        return {"message": f"'{name}'' created successfully!"}, 201

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
    
        if ItemModel.find_by_name(name):  # Update item
            item = ItemModel.find_by_name(name)
            item.price = data['price']
            item.save_to_db()
            return {'message': f"{name} updated successfully!"}, 200

        try:
            item = ItemModel(name, data['price'], data['store_id'])
            item.save_to_db()
        except Exception as err:
            return {"message": f"Could not insert the item: {err}"}, 500

        return {"message": f"'{name}' inserted successfully!"}, 201

    @jwt_required()
    def delete(self, name):
        if ItemModel.find_by_name(name):
            item = ItemModel.find_by_name(name)
            try:
                item.delete()
            except Exception as err:
                return {"message": f"Could not delete the item: {err}"}, 500

            return {"message": f"'{name}' deleted successfully!"}, 200

        return {'message': f"Item '{name}' does not exist!"}, 400
