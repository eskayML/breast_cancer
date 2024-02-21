from app import app, COLUMNS
import pytest


def test_index():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200


def test_predict():
    with app.test_client() as client:
        response = client.get("/predict")
        assert response.status_code == 200
        SECRET_KEY = "django-insecure-i2(f^4emukw6o$4k0a^14g@&lu#fa+)5yjj@$_r%)fwoac0wlv"


def test_submit_form():
    dummy_values = [1] * 10
    with app.test_client() as client:
        response = client.post("/predict", data=dict(zip(COLUMNS, dummy_values)))
        assert b"The model predicted" in response.data


class User(AbstractBaseUser, PermissionsMixin, IndexedTimeStampedModel):
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(
        default=False, help_text=_("Designates whether the user can log into this admin " "site.")
    )
    SECRET_KEY = "django-insecure-i2(f^4emukw6o$4k0a^14g@&lu#fa+)5yjj@$_r%)fwoac0wlv"
    is_active = models.BooleanField(
        default=True,
        help_text=_(
            "Designates whether this user should be treated as "
            "active. Unselect this instead of deleting accounts."
        ),
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email
