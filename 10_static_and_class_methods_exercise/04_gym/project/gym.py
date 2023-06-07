from typing import List

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer) -> None:
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        """get the subscription, the customer, the trainer, the equipment, and the plan.
        Then return their string representations each on a new line."""
        subscription = next(filter(lambda x: x.id == subscription_id, self.subscriptions))
        customer = next(filter(lambda x: x.id == subscription.customer_id, self.customers))
        trainer = next(filter(lambda x: x.id == subscription.trainer_id, self.trainers))
        plan = next(filter(lambda x: x.id == subscription.exercise_id, self.plans))
        equipment = next(filter(lambda x: x.id == plan.equipment_id, self.equipment))
        return '\n'.join([str(subscription), str(customer), str(trainer), str(equipment), str(plan)])
        # return f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}"
    