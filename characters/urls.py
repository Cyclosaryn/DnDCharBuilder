from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('characters/', views.CharacterListView.as_view(), name='character_list'),
    path('characters/<int:pk>/', views.CharacterDetailView.as_view(), name='character_detail'),
    path('characters/create/step1/', views.character_create_step1, name='character_create_step1'),
    path('characters/create/step2/<int:pk>/', views.character_create_step2, name='character_create_step2'),
    path('characters/create/step3/<int:pk>/', views.character_create_step3, name='character_create_step3'),
    path('characters/create/step4/<int:pk>/', views.character_create_step4, name='character_create_step4'),
    path('characters/<int:pk>/edit/', views.CharacterUpdateView.as_view(), name='character_edit'),
    path('characters/<int:pk>/edit/skills/', views.character_edit_skills, name='character_edit_skills'),
    path('characters/<int:pk>/edit/details/', views.character_edit_details, name='character_edit_details'),
    path('characters/<int:pk>/edit/combat/', views.character_edit_combat, name='character_edit_combat'),
    path('characters/<int:pk>/level-up/', views.character_level_up, name='character_level_up'),
    path('characters/<int:pk>/delete/', views.CharacterDeleteView.as_view(), name='character_delete'),
    
    # Spell management
    path('characters/<int:pk>/spells/', views.character_manage_spells, name='character_manage_spells'),
    path('characters/<int:pk>/spell-slots/', views.character_spell_slots, name='character_spell_slots'),
    path('characters/<int:pk>/use-spell-slot/<int:level>/', views.use_spell_slot, name='use_spell_slot'),
    path('characters/<int:pk>/long-rest/', views.long_rest, name='long_rest'),
    path('characters/<int:pk>/short-rest/', views.short_rest, name='short_rest'),
    path('ajax/spell/<int:spell_id>/', views.spell_detail_ajax, name='spell_detail_ajax'),
    path('ajax/equipment/<int:equipment_id>/', views.equipment_detail_ajax, name='equipment_detail_ajax'),
    
    # Reference pages
    path('races/', views.RaceListView.as_view(), name='race_list'),
    path('classes/', views.ClassListView.as_view(), name='class_list'),
    path('backgrounds/', views.BackgroundListView.as_view(), name='background_list'),
]
