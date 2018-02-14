#
# from models import EnumField, Node
#
#
# # class SettingsTest(TestCase):
# #     def test_account_is_configured(self):
# #         assert 'accounts' in INSTALLED_APPS
# #         assert 'accounts.User' == AUTH_USER_MODEL
#
#
# class NodeTest(TestCase):
#     def setUp(self):
#         self.id = "TNenter"
#         self.name = "T North"
#         self.type = EnumField.JOINT
#
#
#         self.test_Node = Node.objects.create_node(
#             id=self.id,
#             name=self.name,
#             type=self.type
#         )
#
#     def test_create_node(self):
#         assert isinstance(self.test_node, Node)
#
#     # def test_default_user_is_active(self):
#     #     assert self.test_user.is_active
#     #
#     # def test_default_user_is_staff(self):
#     #     assert not self.test_user.is_staff
#     #
#     # def test_default_user_is_superuser(self):
#     #     assert not self.test_user.is_superuser
#     #
#     # def test_get_full_name(self):
#     #     assert self.test_user.get_full_name() == 'Test User'
#     #
#     # def test_get_short_name(self):
#     #     assert self.test_user.get_short_name() == self.email
#     #
#     # def test_unicode(self):
#     #     assert self.test_user.__unicode__() == self.username