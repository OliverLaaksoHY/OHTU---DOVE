"""Unit tests for deleting references."""

import unittest
from types import SimpleNamespace
from unittest.mock import patch

import app as app_module


class TestDeleteReference(unittest.TestCase):
    """Verify the delete-reference route behavior."""

    def setUp(self):
        app_module.app.config["TESTING"] = True
        self.client = app_module.app.test_client()
        self.reference = SimpleNamespace(
            id=1,
            title="The Hobbit",
            author="J. R. R. Tolkien",
            year=1937,
        )

    @patch("app.get_reference_by_id")
    def test_get_existing_reference_displays_confirmation(self, get_reference_by_id):
        """Verify that the delete confirmation page is displayed for an existing reference."""
        get_reference_by_id.return_value = self.reference

        response = self.client.get("/delete_reference/1")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Delete Reference", response.data)
        self.assertIn(b"Are you sure you want to delete this reference?", response.data)
        get_reference_by_id.assert_called_once_with(1)

    @patch("app.get_reference_by_id")
    def test_get_missing_reference_returns_404(self, get_reference_by_id):
        """Verify that a 404 is returned when trying to delete a non-existing reference."""
        get_reference_by_id.return_value = None

        response = self.client.get("/delete_reference/1")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, b"Reference not found")
        get_reference_by_id.assert_called_once_with(1)

    @patch("app.db_delete_reference")
    @patch("app.get_reference_by_id")
    def test_post_delete_removes_reference_and_redirects_home(
        self, get_reference_by_id, db_delete_reference
    ):
        """Verify that a reference is deleted and the user is redirected to the home page."""
        get_reference_by_id.return_value = self.reference

        response = self.client.post(
            "/delete_reference/1",
            data={"delete": "Delete"},
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers["Location"], "/")
        get_reference_by_id.assert_called_once_with(1)
        db_delete_reference.assert_called_once_with(1)

    @patch("app.db_delete_reference")
    @patch("app.get_reference_by_id")
    def test_post_without_delete_cancels_and_redirects_to_reference(
        self, get_reference_by_id, db_delete_reference
    ):
        """Verify that deleting a reference is cancelled and 
        the user is redirected to the reference page."""
        get_reference_by_id.return_value = self.reference

        response = self.client.post(
            "/delete_reference/1",
            data={"cancel": "Cancel"},
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers["Location"], "/reference/1")
        get_reference_by_id.assert_called_once_with(1)
        db_delete_reference.assert_not_called()

    @patch("app.db_delete_reference")
    @patch("app.get_reference_by_id")
    def test_post_missing_reference_returns_404_without_deleting(
        self, get_reference_by_id, db_delete_reference
    ):
        """Verify that a 404 is returned when trying to delete a non-existing reference."""
        get_reference_by_id.return_value = None

        response = self.client.post(
            "/delete_reference/1",
            data={"delete": "Delete"},
        )

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, b"Reference not found")
        get_reference_by_id.assert_called_once_with(1)
        db_delete_reference.assert_not_called()
