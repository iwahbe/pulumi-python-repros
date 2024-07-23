import pulumi
import pulumi_random as random

pet = random.Pet("hi", length=3, separator="-")

pulumi.export("result", pet.id)
